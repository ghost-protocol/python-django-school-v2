from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

QUARTER_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
)

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES,default='Male',)
    residence = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.firstname, self.middlename, self.lastname)

class Grade(models.Model):
    user = models.ForeignKey('auth.User')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    sclass = models.CharField(max_length=5)
    classtest1 = models.DecimalField(max_digits=5, decimal_places=2)
    classtest2 = models.DecimalField(max_digits=5, decimal_places=2)
    groupwork = models.DecimalField(max_digits=5, decimal_places=2)
    projectwork = models.DecimalField(max_digits=5, decimal_places=2)
    total50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    examsscore = models.DecimalField(max_digits=5, decimal_places=2)
    exams50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total100 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
           return "%s %s %s" % (self.student, self.subject, self.total100)

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES,default='Male')
    residence = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return "%s %s %s" % (self.firstname, self.middlename, self.lastname)

class Subject(models.Model):
    name =  models.CharField(max_length=50)

    def __str__(self):
    	return self.name

class StudentClass(models.Model):
    name =  models.CharField(max_length=50)

    def __str__(self):
        return self.name

# class TeacherClass(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     tclass =  models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return "%s %s %s" % (self.teacher, self.subject, self.tclass)

#????????????????
class Summary(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sclass = models.CharField(max_length=5, blank=True, null=True)
    total100 = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    totalaverage = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    quarter = models.CharField(max_length=8, choices=QUARTER_CHOICES,default='1st',blank=True, null=True)
    attendance = models.CharField(max_length=10, blank=True, null=True)
    outof = models.CharField(max_length=10, blank=True, null=True)
    comments_classteacher = models.TextField(blank=True, null=True)
    comments_headteacher = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.student, self.sclass)

#ALTER TABLE summary ADD UNIQUE