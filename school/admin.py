from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Grade
from .models import Comment 
#from .models import TeacherClass
from .models import StudentClass

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Comment)
#dmin.site.register(TeacherClass)
admin.site.register(StudentClass)
