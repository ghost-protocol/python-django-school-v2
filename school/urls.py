from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),

    url(r'^student/$', views.student_list, name='student_list'),
    url(r'^student/(?P<pk>\d+)/detail/$', views.student_detail, name='student_detail'),
    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
    # url(r'^student/(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),
    # url(r'^student/(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),

    url(r'^teacher/$', views.teacher_list, name='teacher_list'),
    url(r'^teacher/(?P<pk>\d+)/detail/$', views.teacher_detail, name='teacher_detail'),
    url(r'^teacher/new/$', views.teacher_new, name='teacher_new'),
    url(r'^teacher/(?P<pk>\d+)/edit/$', views.teacher_edit, name='teacher_edit'),

    url(r'^grade/$', views.grade_list, name='grade_list'),
    url(r'^grade/filter/$', views.grade_filter, name='grade_filter'),
    # http://127.0.0.1:8000/grade/search/?subject=Maths&sclass=1A
    # url(r'^grade/search/(?P<subject>\w{1,50})/class/(?P<sclass>\w{1,50})$', views.ClassSubjectSearch, name='ClassSubjectSearch'),
    url(r'^grade/(?P<pk>\d+)/detail/$', views.grade_detail, name='grade_detail'),
    url(r'^grade/new/$', views.grade_new, name='grade_new'),

    url(r'^position/$', views.position_list, name='position_list'),
    url(r'^reporting/$', views.report_student_list, name='report_student_list'),

    url(r'^comment/student/(?P<student_id>\d+)/edit/$', views.comment, name='comment'),
    url(r'^comment/(?P<student_id>\d+)/detail/$', views.comment_detail, name='comment_detail'),
    # url(r"^hellopdf$", HelloPDFView.as_view())
]