from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.db import connection


from django.utils import timezone

from django.shortcuts import redirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Student, Teacher, Grade, TeacherClass

from .forms import StudentForm, TeacherForm, GradeForm, SearchForm

# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"school/home.html")

#############################student
def student_list(request):
    students = Student.objects.order_by('lastname')
    return render(request, 'school/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created = timezone.now()
            student.modified = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'school/student_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            # post.author = request.user
            student.modified = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'school/student_edit.html', {'form': form})
##########################################################
#############################teacher
def teacher_list(request):
    teachers = Teacher.objects.order_by('lastname')
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'school/teacher_detail.html', {'teacher': teacher})

def teacher_new(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.created = timezone.now()
            teacher.modified = timezone.now()
            teacher.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm()
    return render(request, 'school/teacher_edit.html', {'form': form})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            # post.author = request.user
            teacher.modified = timezone.now()
            teacher.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'school/teacher_edit.html', {'form': form})
##########################################################
#############################grade
def grade_list(request):
	if request.user.is_superuser:
		grades = Grade.objects.order_by('student')
		return render(request, 'school/grade_list.html', {'grades': grades})
	else:
		grades = Grade.objects.filter(user = User.objects.get(username=request.user)).order_by('student')
		return render(request, 'school/grade_list.html', {'grades': grades})

def grade_detail(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    return render(request, 'school/grade_detail.html', {'grade': grade})

def grade_new(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = request.user
            grade.total50 = total_50(
            	form.cleaned_data['classtest1'], 
            	form.cleaned_data['classtest2'], 
            	form.cleaned_data['groupwork'], 
            	form.cleaned_data['projectwork']
            	)
            grade.exams50 = float(form.cleaned_data['examsscore']) * 0.5
            grade.total100 = grade.total50 + grade.exams50
            grade.created = timezone.now()
            grade.save()
            return redirect('grade_detail', pk=grade.pk)
    else:
        form = GradeForm()
    return render(request, 'school/grade_new.html', {'form': form})


def total_50(test1, test2, group, project):
	sum = float(test1 + test2 + group + project)
	return(sum * 0.5)

def grade_filter(request):
    if request.method == "GET":
        subject = request.GET.get('subject','')
        sclass = request.GET.get('sclass','')
        # grades = Grade.objects.filter(subject=subject, sclass=sclass)

        if request.user.is_superuser:
		grades = Grade.objects.filter(subject=subject, sclass=sclass)
		return render(request, 'school/grade_list.html', {'grades': grades})
	else:
		grades = Grade.objects.filter(user = User.objects.get(username=request.user), subject=subject, sclass=sclass).order_by('student')
		return render(request, 'school/grade_list.html', {'grades': grades})
        # return render(request, 'school/grade_list.html', {'grades':grades})

#################################################################
#################################################################
# def position_list(request):
    # if request.user.is_superuser:
    # grades = Grade.objects.order_by('-total100')
    # grades = Grade.objects.raw('SELECT sg.id, ss.firstname, ss.lastname, sg.student_id, sg.examsscore, sg.total100, FIND_IN_SET(total100, (SELECT GROUP_CONCAT(DISTINCT total100 ORDER BY total100 desc) FROM school_grade)) as rank FROM school_grade sg, school_student ss where sg.id = ss.id')

        # return HttpResponse(grade.subject)
    # for position, grade in enumerate(grades):
    # return HttpResponse(grades)
    # return render(request, 'school/position_list.html', {'grades': grades})

def position_list(request):
    cursor = connection.cursor()
    subject = 'Maths'
    # sclass  = '1A'
    # ("SELECT sg.id, ss.firstname, ss.lastname, sg.student_id, sg.subject, sg.sclass, sg.examsscore, sg.total100, FIND_IN_SET(total100, (SELECT GROUP_CONCAT(DISTINCT total100 ORDER BY total100 DESC) FROM school_grade WHERE subject = 'Maths' AND sclass = '1A')) AS RANK FROM school_grade sg, school_student ss WHERE sg.subject = 'Maths' AND sg.sclass = '1A' and ss.id = sg.student_id order by sg.total100 desc")
    cursor.execute("SELECT sg.id, ss.firstname, ss.lastname, sg.student_id, sg.subject, sg.sclass, sg.examsscore, sg.total100, FIND_IN_SET(total100, (SELECT GROUP_CONCAT(DISTINCT total100 ORDER BY total100 DESC) FROM school_grade WHERE subject = 'Maths' AND sclass = '1A')) AS RANK FROM school_grade sg, school_student ss WHERE sg.subject = 'Maths' AND sg.sclass = '1A' and ss.id = sg.student_id order by sg.total100 desc")
    grades = cursor.fetchall()
    # return HttpResponse(grades)
    return render(request, 'school/position_list.html', {'grades': grades})
