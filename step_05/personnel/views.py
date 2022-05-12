from turtle import position
from django.shortcuts import render
from django.http import HttpResponse
from personnel.models import Staff

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the personnel index.")

# 查询页面设定
def info(request):
    
    b_sec = request.GET.get('section')
    b_pos = request.GET.get('position')
    b_id = request.GET.get('id')
    b_name = request.GET.get('name')
    
    staffList = Staff.objects.all()
    
    if (b_sec):
        staffList = staffList.filter(section=b_sec)
    if (b_pos):
        staffList = staffList.filter(position=b_pos)
    if (b_id):
        staffList = staffList.filter(id=b_id)
    if (b_name):
        staffList = staffList.filter(name=b_name)
        
    context = {
        'staffList':staffList,
    }              
    return render(request, "personnel/info.html", context)

# 详细信息页面设定
def detail(request, id):
        
    detailInfo = Staff.objects.get(id=id)
    
    context={
        'staff':detailInfo,
    }
    return render(request, "personnel/detail.html",context)