from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework import generics, permissions


class ExamView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = ()


class ExamDetailView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamTaskView(generics.ListAPIView):
    pass


class ExamTaskDetailView(generics.ListAPIView):
    pass


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = ()


class TaskDetailView(generics.ListAPIView):
    pass
