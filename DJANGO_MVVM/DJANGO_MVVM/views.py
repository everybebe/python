
from django.shortcuts import render
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from DJANGO_MVVM.dao_emp import DaoEmp
from anaconda_navigator.utils.py3compat import request
import requests
from nltk.corpus.reader.pl196x import PARA



def index(request):
    return render(request, "index.html")

@csrf_exempt
def ajax(request):
    param = json.loads(request.body)
    print("param",param['menu'])
    context = {
            'result' : 'ok'
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_list(request):
    de = DaoEmp()
    list = de.selectList()
    context = {
            'list' : list
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    param = json.loads(request.body)
    print("param",param['e_id'])
    e_id = param['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    context = {
        'vo' : vo
    } 
    return JsonResponse(context)
    
@csrf_exempt
def ajax_emp_update(request):
    param = json.loads(request.body) 

    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_add(request):
    
    param = json.loads(request.body) 
    
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    print(e_id, e_name, sex, addr)
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)


def ajax_emp_del(request):
    
    param = json.loads(request.body) 
    
    e_id = param['e_id']

    de = DaoEmp()
    cnt = de.delete(e_id)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)
 
 