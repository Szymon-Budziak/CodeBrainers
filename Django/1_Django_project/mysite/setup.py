import os
import django

# migrate
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
django.core.management.execute_from_command_line(['manage.py', 'migrate'])

from polls.models import Question
from django.utils import timezone

# create question object and save it
q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()

# add choices to question object
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
