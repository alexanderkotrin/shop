from django.conf import settings
from django.db import models
# from django.forms import ModelForm
# from django import datetime

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn')

]


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return self.title


GENDER_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


COUNTRY_CHOICES = [
    ('MOLDOVA', 'Moldova'),
    ('ROMANIA', 'Romania'),
    ('GERMANY', 'Germany'),
    ('RUSSIA', 'Rusia'),
    ('ITALY', 'Italy'),
    ('SPAIN', 'Spain'),
    ('FRANCE', 'France')

]


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=25, choices=COUNTRY_CHOICES, default=None)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default=None)
    birth_date = models.DateField(blank=False, null=False)


    def __str__(self):
        return self.last_name



