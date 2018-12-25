# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from app import models
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    return HttpResponse('Hello world!')

    # context = {}
    # context['hello'] = 'hello world!'
    # return render(request, 'hello.html', context)

def index(request):

    cls_list = models.People.objects.all()
    return render(request, 'home.html', {'cls_list':cls_list})

def test(request):
    string = u'我爱学习，学习不爱我'
    return render(request, 'test.html', {'string':string})

def add1(request):
    if request.method == 'GET':
        return render(request, 'add1.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        job = request.POST.get('job')
        year = request.POST.get('year')
        models.People.objects.create(id=id, name=name, sex=sex, year=year, job=job)
        return render(request, 'add2.html')

def add2(request):
    if request.method == 'GET':
        return render(request, 'add2.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        salasy = request.POST.get('salasy')
        Bonus = request.POST.get('Bonus')
        fakuan = request.POST.get('fakuan')
        Overtime_pay = request.POST.get('Overtime_pay')
        models.salasy.objects.create(id=id, name=name, sex=sex, salasy=salasy, Bonus=Bonus, fakuan=fakuan, Overtime_pay=Overtime_pay)
        return render(request, 'succeed.html')
@csrf_exempt
def dels(request):
    if request.method == 'GET':
        return render(request, 'dels.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        models.People.objects.filter(id=id).delete()
        return render(request, 'succeed.html')
def find(request):
    return render(request, 'find.html')
def print(request):
    return render(request, 'print.html')

def edit(request):
    pass
