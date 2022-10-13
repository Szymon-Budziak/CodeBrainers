from django.contrib.auth import get_user_model
from rest_api.models import Exam

# create User
users = get_user_model()
admin = users.objects.all()[0]

# create two Exam objects and save them
exam1 = Exam(name="Math", owner=admin, description="Non linear algebra", final_grade=4)
exam1.save()

exam2 = Exam(name="Physics", owner=admin, description="Thermodynamics", final_grade=5)
exam2.save()

# add tasks to exams
exam1.task_set.create(name="Basic equations", description="Basic equations task", points=4, exam=exam1)
exam2.task_set.create(name="Basic thermodynamics", description="Zeroth law", points=5, exam=exam2)
