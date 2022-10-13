import os
import django

# migrate
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_rest.settings'
django.setup()
django.core.management.execute_from_command_line(['manage.py', 'migrate'])

from bookreview.models import Author, Book

# create two Author objects and save them
author1 = Author("Adam", "Mickiewicz")
author1.save()

author2 = Author("Jane", "Austen")
author2.save()

# add books to authors
author1.book_set.create(title="Pan Tadeusz", isbn="978-0781800334", author=author1)
author2.book_set.create(title="The Three Sisters", isbn="978-1250276896", author=author2)
