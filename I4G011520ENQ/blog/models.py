from msilib.schema import Class
from operator import length_hint
from django.db import models
from hamcrest import none
from sqlalchemy import ForeignKey

# Create your models here.
class Post (models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateField
    Published_date = models.DateTimeField
