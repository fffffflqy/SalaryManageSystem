# -*- coding:utf-8 -*-
from django.http import HttpResponse
from app.models import People, salary, user


def testdb(request):
    test1 = People(id=101, name='吴进军', sex='男', year=6, job='老板', department='督导层')
    test2 = salary(id=101, name='lqy', salary=100, Bonus=0, fakuan=50, Overtime_pay=200)
    test3 = user(user='huas_lqy', password='123456')
    test1.save()
    test2.save()
    test3.save()
    return HttpResponse("<p>数据添加成功!</p>")
