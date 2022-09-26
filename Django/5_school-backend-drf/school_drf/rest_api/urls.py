from django.urls import path
from .views import ExamView, ExamDetailView, ExamTaskView, ExamTaskDetailView, TaskView, TaskDetailView

urlpatterns = [
    path('exams/', ExamView.as_view(), name="exams"),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name="exam"),
    path('exams/<int:pk>/tasks/', ExamTaskView.as_view(), name="exam-tasks"),
    # path('exams/<int:pk>/tasks/<int:pk>/', ExamTaskDetailView.as_view(), name="exam-task"),
    path('tasks/', TaskView.as_view(), name="tasks"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name="task"),
]
