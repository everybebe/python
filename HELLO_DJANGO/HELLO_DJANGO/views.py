from django.http import HttpResponse
from sympy.polys.polyconfig import query
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from anaconda_navigator.utils.py3compat import request
from conda.base.context import context
from HELLO_DJANGO import dao_emp



def index(request):
    return HttpResponse("<h1>hello django.</h1><br><h2>hello django.</h2>")

def param(request):
    menu = request.GET.get('menu', '탕수육')
    return HttpResponse("param:{}".format(menu))

@csrf_exempt
def post(request):
    menu = request.POST['menu']
    return HttpResponse("post:{}".format(menu))

def forw(request):
    a = "홍길동"
    b = ["손흥민","이강인","김민재"]
    c= [
        {'e_id':'1', 'e_name':'1','sex':'1','addr':'1'},
        {'e_id':'2', 'e_name':'2','sex':'2','addr':'2'},
        {'e_id':'3', 'e_name':'3','sex':'3','addr':'3'},
        ]
    return render(request, "forw.html",{"data":b,"data2":a,"data3":c})


def emp(request):
    de = dao_emp.DaoEmp()
    list = de.selectList()
        
    return render(request,"emp.html",{'list' : list})