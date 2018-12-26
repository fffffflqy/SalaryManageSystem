# -*- coding:utf-8 -*-
from django.http import HttpResponse
from app.models import People, salary, user


def testdb(request):
    test1 = People(id=1, name='lqy', sex='男', year=20, job='苦力')
    test2 = salary(id=1, name='lqy', salary=100, Bonus=0, fakuan=50, Overtime_pay=200)
    test3 = user(user='lqy', admin=1, password='123456')
    test1.save()
    test2.save()
    test3.save()
    return HttpResponse("<p>数据添加成功!</p>")