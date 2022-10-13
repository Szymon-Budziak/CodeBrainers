import os
import django
from django.contrib.auth.models import User

# migrate
os.environ['DJANGO_SETTINGS_MODULE'] = 'rest_api.settings'
django.setup()
django.core.management.execute_from_command_line(['manage.py', 'migrate'])

from rest_api.models import Exam

# create two User objects
user1 = User.objects.create_user("user1", "user1@ex.com", None)

user2 = User.objects.create_user("user2", "user2@ex.com", None)

# create two Exam objects and save them
exam1 = Exam(name="Math", owner=user1, description="Non linear algebra", final_grade=4)
exam1.save()

exam2 = Exam(name="Physics", owner=user2, description="Thermodynamics", final_grade=5)
exam2.save()

# add tasks to exams
exam1.task_set.create(name="Basic equations", description="Basic equations task", points=4, exam=exam1)
exam2.task_set.create(name="Basic thermodynamics", description="Zeroth law", points=5, exam=exam2)
