from .views import *
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

router.register("exams", ExamView, basename="exams"). \
    register("tasks", TaskView, basename="exams-tasks", parents_query_lookups=['exam'])

router.register("tasks", TaskView, basename="tasks")
urlpatterns = router.urls
