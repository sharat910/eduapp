from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    cid = models.CharField(max_length=50)
    nooflectures = models.IntegerField()
    instructorname = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=100)
    duration = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
		return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=100)
    lecid = models.IntegerField()
    videoid = models.CharField(max_length=100)
    duration = models.IntegerField()
    course = models.ForeignKey(Course)
    audio = models.FileField(upload_to="files/%Y/%m/%d",null = True,blank=True)

    def __unicode__(self):
		return self.name

class Student(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    age = models.IntegerField( null=True)
    course_comp = models.ManyToManyField(Course,related_name='cc')
    course_prog = models.ManyToManyField(Course,related_name='cp')

    def __unicode__(self):
		return self.name
