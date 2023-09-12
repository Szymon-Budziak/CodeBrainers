from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@ex.com'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='Test title',
            text='Test text',
        )

    def test_post_creation(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.text, 'Test text')
        self.assertTrue(self.post.created_date <= timezone.now())
        self.assertIsNone(self.post.published_date)

    def test_publish_method(self):
        self.post.publish()

        self.assertIsNotNone(self.post.published_date)
        self.assertTrue(self.post.published_date <= timezone.now())
        self.assertTrue(self.post.created_date <= self.post.published_date)

    def test_str_method(self):
        self.assertEqual(str(self.post), 'Test title')


class PostListTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@ex.com'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='Test post',
            text='Test text'
        )

    def test_post_list_view_with_published_post(self):
        self.post.publish()

        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('Test post', response.content.decode())
        self.assertContains(response, 'Test post')
        self.assertIn('Test text', response.content.decode())

    def test_post_list_view_with_unpublished_post(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Test post', response.content.decode())
        self.assertNotIn('Test text', response.content.decode())
