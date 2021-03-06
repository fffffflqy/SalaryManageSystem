# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from app import models
from django.views.decorators.csrf import csrf_exempt
M_user = ''

def hello(request):
    return HttpResponse('Hello world!')

    # context = {}
    # context['hello'] = 'hello world!'
    # return render(request, 'hello.html', context)
@csrf_exempt
def login(request):
    global M_user
    if request.method == 'GET':
        M_user = ''
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user').strip()
        # print(type(user))
        if not models.user.objects.filter(user=user):
            return render(request, 'Login_error.html',{'error_info': '用户不存在'})
        password = request.POST.get('password').strip()
        db_passwd = models.user.objects.get(user=user).password
        if password == db_passwd:
            M_user = user
            return render(request, "main.html", {'name':user})
        else:
            return render(request, 'login_error.html', {'error_info': '密码错误'})

def main(request):
    global M_user
    if M_user == '' :
        return render(request, 'login_error.html', {'error_info': '请先登入'})
    else :
        return render(request, 'main.html', {'name':M_user})

def show_people(request):
    global M_user
    if request.method == 'GET':
        people_list = models.People.objects.all()
        return render(request, 'show_every_people.html', {'people_list':people_list})
    elif request.method == 'POST':
        id = request.POST.get('search_people')
        department = request.POST.get('department')
        if id == '':
            people_list = models.People.objects.all()
        elif id is None:
            people_list = models.People.objects.filter(department=department)
            return render(request, 'show_every_people.html', {'people_list': people_list})
        else :
            if models.People.objects.filter(id=id):
                people_list = [models.People.objects.get(id=id)]
            else:
                return render(request, 'succeed.html', {'error_info': '未查到此id', 'error_in':'返回首页'})

        return render(request, 'show_every_people.html', {'people_list':people_list})

def show_salary(request):
    global M_user
    if request.method == 'GET':
        salary_list = models.salary.objects.all()
        return render(request, 'show_every_salary.html', {'salary_list': salary_list})
    elif request.method == 'POST':
        id = request.POST.get('search')
        if id == '':
            salary_list = models.salary.objects.all()
        else:
            salary_list = [models.salary.objects.get(id=id)]
        return render(request, 'show_every_salary.html', {'salary_list': salary_list})

def update_people(request):
    if request.method == 'GET':
        id = request.GET['id']
        people_list = [models.People.objects.get(id=id)]
        # people_list = models.People.objects.all()
        return render(request, 'update_people.html', {'people_list':people_list})
    elif request.method == 'POST':
        id = request.GET['id']
        people = models.People.objects.get(id=id)
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        job = request.POST.get('job')
        year = request.POST.get('year')
        department = request.POST.get('department')
        if name != '':
            people.name = name
        if sex != '':
            people.sex = sex
        if job != '':
            people.job = job
        if year != '':
            people.year = year
        if department != '':
            people.department = department
        people.save()
        return render(request, 'succeed.html',{'error_info': '修改成功', 'error_in':'返回员工列表'})

def update_salary(request):
    if request.method == 'GET':
        id = request.GET['id']
        salary_list = [models.salary.objects.get(id=id)]
        return render(request, 'update_salary.html', {'salary_list':salary_list})
    elif request.method == 'POST':
        id = request.GET['id']
        Salary = models.salary.objects.get(id=id)
        salary = request.POST.get('salary')
        name = request.POST.get('name')
        Bonus = request.POST.get('Bonus')
        fakuan = request.POST.get('fakuan')
        Overtime_pay = request.POST.get('Overtime_pay')
        note = request.POST.get('note')
        if name != '':
            Salary.name = name
        if salary != '':
            Salary.salary = salary
        if Bonus != '':
            Salary.Bonus = Bonus
        if fakuan != '':
            Salary.fakuan = fakuan
        if Overtime_pay != '':
            Salary.Overtime_pay = Overtime_pay
        Salary.note = note
        Salary.save()
        return render(request, 'succeed.html',{'error_info': '修改成功', 'error_in':'返回工资列表'})

def insert_people(request):
    if request.method == 'GET':
        return render(request, 'insert_people.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        job = request.POST.get('job')
        year = request.POST.get('year')
        department = request.POST.get('department')
        models.People.objects.create(id=id, name=name, sex=sex, year=year, job=job, department=department)
        return render(request, 'succeed.html', {'error_info': '添加成功', 'error_in':'返回员工列表'})

def insert_salary(request):
    if request.method == 'GET':
        return render(request, 'insert_salary.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        salary = request.POST.get('salary')
        Bonus = request.POST.get('Bonus')
        fakuan = request.POST.get('fakuan')
        Overtime_pay = request.POST.get('Overtime_pay')
        note = request.POST.get('note')
        models.salary.objects.create(id=id, name=name, salary=salary, Bonus=Bonus, fakuan=fakuan, Overtime_pay=Overtime_pay, note=note)
        return render(request, 'succeed.html', {'error_info': '添加成功', 'error_in':'返回工资列表'})

def pay(request):
    if request.method == 'GET':
        salary_list = models.salary.objects.all()
        tot_list = []
        for salary in salary_list:
            tot_list.append({'id':salary.id, 'name':salary.name, 'tot_salary':salary.salary+salary.Bonus-salary.fakuan+salary.Overtime_pay})

        return render(request, 'pay.html', {'tot_list':tot_list})

def index(request):
    global M_user
    cls_list = models.People.objects.all()
    return render(request, 'home.html', {'cls_list':cls_list})

def test(request):
    string = u'我爱学习，学习不爱我'
    return render(request, 'test.html', {'string':string})

def dels(request):
    if request.method == 'GET':
        return render(request, 'del_people.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        models.People.objects.filter(id=id).delete()
        models.salary.objects.filter(id=id).delete()
        return render(request, 'succeed.html',{'error_info': '删除成功', 'error_in':'返回首页'})
def find(request):
    return render(request, 'find.html')
def print(request):
    return render(request, 'print.html')









def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')


def change_ps(request):
    if request.method == 'GET':
        return render(request, 'change_ps.html')
    elif request.method == 'POST':
        User = models.user.objects.get(user=M_user)
        password1 = request.POST.get('passworld1')
        password2 = request.POST.get('passworld2')
        if password1 == password2 and password1 != '':
            User.password = password1
            User.save()
            render(request, 'succeed.html', {'error_info': '修改成功', 'error_in':'返回首页'})
        else :
            render(request, 'succeed.html', {'error_info': '修改失败请重新尝试', 'error_in':'返回首页'})


