from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsExamOwnerOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.viewsets import ModelViewSet


class ExamView(NestedViewSetMixin, ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class TaskView(NestedViewSetMixin, ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsExamOwnerOrReadOnly)
