from django.db import models
import datetime
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

   
class Student(models.Model):
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    dob=models.DateField(default=datetime.date.today)
    address=models.TextField(default="")
    contact=models.CharField(max_length=50, default="")
    stuimg=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.fname + " " + self.mname + " " + self.lname


class StudentResult(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    min_marks=models.IntegerField()
    marks_obt=models.IntegerField()


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profileImg=models.ImageField(upload_to='profile_img',default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'