from django import forms
from .models import Student
from .models import Teacher
from .models import Grade
from .models import Comment
from django.contrib.auth.forms import AuthenticationForm 


from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

class StudentForm(forms.ModelForm):
        
    class Meta:
        model = Student
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'dateofbirth',
            'gender',
            'residence',
            'address',
            'contact',
            'email'
        ]

    def __init__(self, *args, **kwargs):
       super(StudentForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-student-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('Personal',
                    # Field('firstname', placeholder='first name', css_class="some-class"),
                    Field('firstname', css_class="some-class"),
                    Field('middlename', css_class="some-class"),
                    Field('lastname', css_class="some-class"),
                    Field('dateofbirth', placeholder='yyyy-mm-dd', css_class="some-class"),
                    Field('gender', css_class="some-class"),),
           Fieldset('Contact', 'email', 'contact'),)
           # Fieldset('Contact data', 'email', 'contact', style="color: brown;"),)

       # self.helper = FormHelper()
       # self.helper.form_id = 'id-student-form'
       # self.helper.form_method = 'post'
       # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))

class TeacherForm(forms.ModelForm):
        
    class Meta:
        model = Teacher
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'dateofbirth',
            'gender',
            'residence',
            'address',
            'contact',
            'email'
        ]

    def __init__(self, *args, **kwargs):
       super(TeacherForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-teacher-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('Personal',
                    # Field('firstname', placeholder='first name', css_class="some-class"),
                    Field('firstname', css_class="some-class"),
                    Field('middlename', css_class="some-class"),
                    Field('lastname', css_class="some-class"),
                    Field('dateofbirth', placeholder='yyyy-mm-dd', css_class="some-class"),
                    Field('gender', css_class="some-class"),),
           Fieldset('Contact', 'email', 'contact'),)

########################################################
#######################grade form

class GradeForm(forms.ModelForm):
        
    class Meta:
        model = Grade
        fields = [
            'student',
            'subject',
            'sclass',
            'classtest1',
            'classtest2',
            'groupwork',
            'projectwork',
            'examsscore',
        ]

    def __init__(self, *args, **kwargs):
       super(GradeForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-grade-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       # self.helper.layout = Layout(
       #     Fieldset(
       #              Field('student', css_class="some-class"),
       #              # Field('subject', css_class="some-class"),
       #              # Field('classtest1', css_class="some-class"),
       #              # Field('classtest2', css_class="some-class"),
       #              # Field('groupwork', css_class="some-class"),
       #              # Field('projectwork', css_class="some-class"),
       #              # Field('total50', css_class="some-class"),
       #              # Field('examsscore', css_class="some-class"),
       #              # Field('total100', css_class="some-class"),
       #          )
       #      )



class ClassSubjectSearchForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)


class SearchForm(forms.Form):

    STUDENT_CLASS = (  
      ('1A', '1A'),
      ('2A', '2A'),
    )
    
    STUDENT_SUBJECT = (  
      ('Maths', 'Maths'),
      ('Science', 'Science'),
      ('English', 'English'),
      ('ICT', 'ICT'),
      ('French', 'French'),
    )

    USER_ROLE = (  
      ('Teacher', 'Teacher'),
      ('HeadTeacher', 'HeadTeacher'),
    )

    student_sclass = forms.ChoiceField(choices=STUDENT_CLASS)
    student_subject = forms.ChoiceField(choices=STUDENT_SUBJECT)


class LoginForm(AuthenticationForm):
  username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
  password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(forms.Form):
  username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
  password1 = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput())
  password2 = forms.CharField(label='Password(Again)', max_length=30, widget=forms.PasswordInput())
  role     = forms.CharField(label="role", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'role'}))

class CommentForm(forms.ModelForm):
  class Meta:
        model = Comment
        fields = [
            'student',
            'sclass',
            'total100',
            'totalaverage',
            'quarter',
            'attendance',
            'outof',
            'comments_classteacher',
            'comments_headteacher',
        ]
  def __init__(self, *args, **kwargs):
       super(CommentForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-comment-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       # self.helper.Field('student', readonly=True)
       # self.fields['student'].widget.attrs['readonly'] = True
       # self.helper.layout = Layout('student', readonly=True)


  