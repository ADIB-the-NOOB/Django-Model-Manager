import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelManager.settings')

import django
# Import settings
django.setup()




from faker import Faker
faker = Faker()
from base.models import Student
import random


def generate_students():
    for i in range(100):
        name = faker.name()
        age = random.randint(18, 30)
        is_deleted = random.choice([True, False])
        address = faker.address()
        birthday = faker.date()
        info = faker.text()
        Student.objects.get_or_create(name=name, age=age,is_deleted=is_deleted, address=address, birthday=birthday, info=info)


# Call the function for inserting data into database.
generate_students()