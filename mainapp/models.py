from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User, auth

# Create your models here.
class Schedule1(models.Model):
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Schedule2(models.Model):
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Schedule3(models.Model):
    img = models.ImageField(upload_to ='pics')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Highlight(models.Model):
    image = models.ImageField(upload_to ='pics')
    work = models.CharField(max_length=100)
    worktype = models.CharField(max_length=200)
    description = models.TextField()

class Inquiry(models.Model):
    first_name = models.CharField(max_length=50)
    interview = models.BooleanField(default=False)
    work_or_commision = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    email = models.EmailField()
    Details = models.TextField()

class ExtendedUser(models.Model):
    CD_Id = models.OneToOneField(User, on_delete=CASCADE)
    dateofbirth = models.DateField()
    phone = models.CharField(max_length=20)



    