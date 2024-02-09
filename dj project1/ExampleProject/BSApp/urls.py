from django.urls import path
from BSApp import views
urlpatterns=[
	path('',views.home,name="hme"),
	path('abt/',views.about,name="ab"),
	path('std/',views.student,name="stud"),
	path('sp/<int:k>/',views.stdup,name="stpd"),
	path('ds/<int:n>/',views.stdel,name="sd"),
	path('empl/',views.emp,name="em"),
	path('emup/<int:z>/',views.emupd,name="empd"),
	path('emdp/<int:o>/',views.emdelete,name="emd"),
]
