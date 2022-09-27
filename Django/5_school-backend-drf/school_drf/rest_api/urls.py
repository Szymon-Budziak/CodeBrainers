from django.urls import path
from .views import ExamView, ExamDetailView, ExamTaskView, ExamTaskDetailView, TaskView, TaskDetailView

urlpatterns = [
    path('exams/', ExamView.as_view(), name="exams"),
    path('exams/<int:exam_id>/', ExamDetailView.as_view(), name="exam"),
    path('exams/<int:exam_id>/tasks/', ExamTaskView.as_view(), name="exam-tasks"),
    path('exams/<int:exam_id>/tasks/<int:task_id>/', ExamTaskDetailView.as_view(), name="exam-task"),
    path('tasks/', TaskView.as_view(), name="tasks"),
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name="task"),
]
