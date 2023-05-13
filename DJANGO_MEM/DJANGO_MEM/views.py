from django.http import HttpResponse
from sympy.polys.polyconfig import query
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from DJANGO_MEM.dao_emp import DaoMem




def mem_list(request):
    de = DaoMem()
    list = de.selectList()
    return render(request,"mem_list.html",{'list' : list})


def mem_detail(request):
    m_id = request.GET.get('m_id', '')
    de = DaoMem()
    vo = de.selectOne(m_id)
    return render(request,"mem_detail.html",{'vo' : vo})

def mem_mod(request):
    m_id = request.GET.get('m_id', '')
    de = DaoMem()
    vo = de.selectOne(m_id)
    return render(request,"mem_mod.html",{'vo' : vo})

def mem_mod_act(request):
    m_id = request.POST.get('m_id')
    m_name = request.POST.get('m_name')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    
    de = DaoMem()
    cnt = de.update(m_id, m_name, tel, address)
    
    return render(request,"mem_mod_act.html",{'cnt' : cnt})

def mem_add(request):
       
    return render(request,"mem_add.html")

def mem_add_act(request):
    m_id = request.POST.get('m_id')
    m_name = request.POST.get('m_name')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    
    de = DaoMem()
    cnt = de.insert(m_id, m_name, tel, address)
    
    return render(request,"mem_add_act.html",{'cnt' : cnt})


def mem_del_act(request):
    m_id = request.POST.get('m_id')
    
    de = DaoMem()  
    cnt = de.delete(m_id)
         
    return render(request,"mem_del_act.html",{'cnt' : cnt})
