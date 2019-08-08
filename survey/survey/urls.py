"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path

from survey import views

urlpatterns = [
    path('',views.index),
    path('add/', views.addView),
    path('success/', views.addSuccess),
    path('firstRegister/', views.sendRegisterEmail),
    path('nameCheck/', views.nameCheck),
    path('emailCheck/', views.emailCheck),
    path('loginAction/', views.loginAction),
    path('user/', views.userView),
    path('deletePaper/',views.deleteAction),
    path('modifySuccess/',views.saveModifyAction),
    path('releasePaper/',views.releasePaperAction),
    re_path(r'^a/AkdjrEkclaoq/(.*)', views.secondRegister),
    re_path(r'^modify/(.*)', views.modifyView),
    re_path(r'^paper/(.*)', views.paperView),
    re_path(r'^.*', views.erro),
    #re_path(r'/*',views.erro),
]
