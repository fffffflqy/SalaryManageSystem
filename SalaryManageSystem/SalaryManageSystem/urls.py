"""SalaryManageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from . import view, testdb


urlpatterns = [
    path('', view.index),
    path('admit/', admin.site.urls),
    path('hello/', view.hello),
    path('testdb/', testdb.testdb),
    path('test/', view.test),
    path('index/', view.index, name ='index'),
    path('add1/', view.add1, name='add1'),
    path('add2/', view.add2, name='add2'),
    path('dels/', view.dels, name='del'),
    path('find/', view.find, name='find'),
    path('print/', view.print, name='print'),
    path('edit/', view.edit, name='edit')
]