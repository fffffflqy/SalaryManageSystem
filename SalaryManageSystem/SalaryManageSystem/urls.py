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
from . import view, testdb, input_csv


urlpatterns = [
    path('', view.login),
    path('admit/', admin.site.urls),
    path('hello/', view.hello),
    path('input_people/', input_csv.input_people),
    path('input_salary/', input_csv.input_salary),
    # path('testdb/', testdb.testdb),
    path('login/', view.login),
    path('test/', view.test),
    path('main/', view.main, name='main'),
    path('dels/', view.dels, name='del'),
    path('find/', view.find, name='find'),
    path('print/', view.print, name='print'),
    path('show_every_people/', view.show_people),
    path('show_every_salary/', view.show_salary),
    path('update_people/', view.update_people),
    path('update_salary/', view.update_salary),
    path('insert_people/', view.insert_people),
    path('del_people/', view.dels),
    path('insert_salary/', view.insert_salary),
    path('register/', view.register),
    path('change_ps/', view.change_ps),
    path('pay/', view.pay)
]