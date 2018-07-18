import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
application = get_wsgi_application()

import random
import string
import json
from faker import Faker

from employee_app.models import Employee
from django.contrib.auth.models import User

faker = Faker()

users = [
   User.objects.create_user(username='larry', email='larry@awesome.org', password='hello'),
]



for i in range(0,50):
    
    e = Employee()
    e.FirstName = faker.first_name()
    e.LastName = faker.last_name()
    e.MiddleInitial = random.choice(string.ascii_letters)

    e.DateOfBirth = faker.date()
    e.DateOfEmployment = faker.date()
    e.Status = True

    e.save()