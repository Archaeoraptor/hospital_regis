# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .form import *
from django.http import HttpResponse
from hos.models import *
from itertools import groupby
import pandas as pd
# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         patient = PatientForm()
#         return render(request, 'data_form.html', locals())
#     else:
#         patient = PatientForm(request.POST)
#         if patient.is_valid():
#             cname = patient.cleaned_data['name']
#             return HttpResponse('<h4>hello,word!</h4>')
#         else:
#             error_msg = patient.errors.as_json()
#             print(error_msg)
#             return render(request, 'data_form.html', locals())


def statistic(request):
    #
    # name_list = Patient2.objects.values('name_patient', 'id_card')

    sum_s = Patient2.objects.values('sex')
    sum_a = Patient2.objects.values('age')
    sum_d = Patient2.objects.values('doctor')
    sum_o = Patient2.objects.values_list('office')
    # 性别统计
    sum_patient_sex = [str(sum_s).count("1"), str(sum_s).count("2")]
    # 强制转为list
    # sum = []
    # for x in sum_s:
    #     sum.append(int(x.get('doctor')))

    list_t = []
    for i in range(0, 130):
        list_t.append(str(sum_a).count(str(i)))

    sum_patient_age = [len(sum_a)-sum(list_t[19:130]), sum(list_t[19:45]), sum(list_t[46:60]), sum(list_t[61:130])]

    sum_doctor = [str(sum_d).count("1"),
                  str(sum_d).count("2"),
                  str(sum_d).count("3"),
                  str(sum_d).count("4"),
                  str(sum_d).count("5"),
                  str(sum_d).count("6"),
                  str(sum_d).count("7"),
                  str(sum_d).count("8"),
                  str(sum_d).count("9"),
                  str(sum_d).count("10"),
                  str(sum_d).count("11"),
                  0
                  ]
    # for i in set(sum_d):
    #     sum_doctor[i] = str(sum_d).count(i)
    sum_office = [str(sum_o).count("1"),
                  str(sum_o).count("2"),
                  str(sum_o).count("3"),
                  str(sum_o).count("4"),
                  str(sum_o).count("5"),
                  str(sum_o).count("6"),
                  str(sum_o).count("7"),
                  str(sum_o).count("8"),
                  str(sum_o).count("9"),
                  str(sum_o).count("10"),
                  str(sum_o).count("11"),
                  0
                  ]
    title = '统计'
    return render(request, 'statistic_page.html', context=locals(), status=200)

# for k, g in groupby(sorted(lst), key=lambda x: x//50):
#     print('{}-{}: {}'.format(k*50, (k+1)*50-1, len(list(g))))

