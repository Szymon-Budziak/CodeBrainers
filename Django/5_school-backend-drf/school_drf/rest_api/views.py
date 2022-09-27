from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsExamOwnerOrReadOnly


class ExamView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = ()
    lookup_url_kwarg = "exam_id"


class ExamTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = ()
    lookup_url_kwarg = "exam_id"

    def perform_create(self, serializer):
        serializer.save(exam_id=self.kwargs["pk"])


class ExamTaskDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = ()
    lookup_url_kwarg = "task_id"

    def get_queryset(self):
        task = self.kwargs["task_id"]
        return Task.objects.get(id=task)


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsExamOwnerOrReadOnly)


class TaskDetailView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = ()
    lookup_url_kwarg = "task_id"
