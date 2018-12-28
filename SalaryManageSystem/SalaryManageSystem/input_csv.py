# -*- coding:utf-8 -*-
import csv
from django.http import HttpResponse
from app.models import People, salary, user


def input_people(request):
    result = []
    with open('D:\python\工资管理系统\SalaryManageSystem\database_people.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for items in reader:
            if reader.line_num == 1:
                continue
            test=People(id=int(items[0]), name=items[1], sex=items[2], year=int(items[3]), job=items[4], department=items[5])
            test.save()
    return HttpResponse('ok')

def input_salary(request):
    result = []
    # people_list = People.objects.all()
    # for people in people_list:
    #     People.objects.filter(id=people.id).delete()
    with open('D:\python\工资管理系统\SalaryManageSystem\database_salary.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for items in reader:
            if reader.line_num == 1:
                continue
            test=salary(id=int(items[0]), name=items[1], salary=int(items[2]), Bonus=int(items[3]), fakuan=int(items[4]), Overtime_pay=int(items[5]), note=items[6])
            test.save()
    return HttpResponse('ok')