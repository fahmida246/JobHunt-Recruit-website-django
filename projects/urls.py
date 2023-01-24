from django.contrib import admin
from django.urls import path,include
from projects import views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name='home'),
    
    path("loginpage",views.loginpage, name='loginpage'),
    path("loginpage2",views.loginpage2, name='loginpage2'),
    path("logoutuser",views.logoutuser, name='logoutuser'),
    path("signin", views.signin,name='signin'),
    path("signin2", views.signin2,name='signin2'),


    path("contact",views.contact,name='contact'),
    path("contactcompany",views.contactcompany,name='contactcompany'),
    path("contactcandidate",views.contactcandidate,name='contactcandidate'),
    path("cvtips", views.cvtips,name='cvtips'),
    path("jobs", views.jobs,name='jobs'),
    path("search", views.search,name='search'),


    path("createjobs", views.createjobpost,name='createjobs'),
	path('deletejobpost/<str:pk>/', views.deletejob, name='deletejobpost'),
    path('appliedcandidate', views.appliedcandidate, name='appliedcandidate'),
    path('feedback', views.sendfeedback, name='feedback'),
    
    path('updatejob/<int:job_id>/',views.updatejob,name='updatejob'),
    path('deletejob/<int:job_id>/',views.deletejob,name="deletejob"),
  



    path("applyforjobs", views.applyforjobs,name='applyforjobs'),
    path("searchforjob", views.searchforjob,name='searchforjob'),
    path('apply', views.apply, name='apply'),
    path('showjobs', views.showjobs, name='showjobs'),
    path('profileforcandidate', views.profileforcandidate, name='profileforcandidate'),
    path('profileforcompany', views.profileforcompany, name='profileforcompany'),
    path('editforcandidate', views.editforcandidate, name='editforcandidate'),
    path('editforcompany', views.editforcompany, name='editforcompany'),
    path('changepasswordforcandidate', views.changepasswordforcandidate, name='changepasswordforcandidate'),
    path('changepasswordforcompany', views.changepasswordforcompany, name='changepasswordforcompany'),
    path('viewmyuploadedjobs', views.viewmyuploadedjobs, name='viewmyuploadedjobs'),

    path('getfeedback', views.getfeedback, name='getfeedback'),


    path('login_admin', views.login_admin, name='login_admin'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('change_passwordadmin', views.change_passwordadmin, name='change_passwordadmin'),
    path('adminviewjobs', views.adminviewjobs, name='adminviewjobs'),
    path('adminviewcompany', views.adminviewcompany, name='adminviewcompany'),
    path('adminviewcandidate', views.adminviewcandidate, name='adminviewcandidate'),
    path('adminviewcontact', views.adminviewcontact, name='adminviewcontact'),

    
    path('viewcandidateapplication', views.viewcandidateapplication, name='viewcandidateapplication'),
    path('updatecandidateform/<int:candidate_id>/', views.updatecandidateform, name='updatecandidateform'),

    path('applyjob', views.applyjob, name='applyjob'),










    
    




] 