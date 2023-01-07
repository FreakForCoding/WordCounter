"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from turtle import home
from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('adminwc/', views.adminwc, name='admin'),

    path('',views.home),
    path('signup/',include("signup.urls")),
    #path('count/',views.count),
    path('home/',views.home, name="home"),
    #path('signup/', views.signupview, name='signup'),
    path('login/', views.login, name='login'),

    path('logout/', views.userLogout, name='logout'),

   

    path('userLogin/signup', views.signupaction, name='signup'),


    path('signup/',views.signup,name='signup'),

    path('usersignup/',views.usersignup,name='usersignup'),


    #features

    path('features/',views.features,name='features'),
    path('features/home.html',views.home,name='home'),
    path('features/signup.html',views.signup,name='home'),
    path('features/features',views.features,name='features2'),
    path('features/signup',views.signup,name='signup'),
    path('features/login',views.login,name='login'),
    path('features/home',views.home,name='home'),


    #path('home/',views.home,name='home'),
    #path('home/',views.home),


    path("contact", views.contact, name="contact"),





    #userlogin
     path('userLogin/', views.userLogin, name='userLogin'),

    path('userLogin/logout', views.userLogout, name='userLogout'),

    path('userLogin/login', views.login, name='login'),
    path('userLogin/signup.html',views.signup,name='home'),
    path('userLogin/features',views.features,name='features2'),
    path('userLogin/signup',views.signup,name='signup'),
    path('userLogin/login',views.login,name='login'),
    path('userLogin/contact',views.contact,name='contact'),
    path('userLogin/home',views.home,name='home'),



    #home
    path('home/home.html',views.home,name='home'),
    path('home/signup.html',views.signup,name='home'),
    path('home/features',views.features,name='features2'),
    path('home/signup',views.signup,name='signup'),
    path('home/login',views.login,name='login'),
    path('home/contact',views.contact,name='contact'),
    path('home/home',views.home,name='home'),


]
