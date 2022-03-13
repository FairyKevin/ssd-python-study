from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# 查询页面设定
staffList = [
    {'id':'D00001','name':'张吉惟','section':'开发部','position':'员工','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00002','name':'林国瑞','section':'开发部','position':'主管','sex':'男','edu':'硕士','birthday':'1978-04-21','entry':'2010-07-01'},
    {'id':'D00003','name':'刘姿婷','section':'财务部','position':'主管','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00004','name':'夏志豪','section':'开发部','position':'员工','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00005','name':'郑伊雯','section':'人事部','position':'主管','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00006','name':'林玟书','section':'宣传部','position':'主管','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00007','name':'江奕云','section':'运营部','position':'主管','sex':'男','edu':'说是','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00008','name':'荣姿康','section':'开发部','position':'主管','sex':'男','edu':'硕士','birthday':'1978-04-21','entry':'2010-07-01'},
    {'id':'D00009','name':'吴心真','section':'财务部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00010','name':'李雅惠','section':'开发部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00011','name':'周逸珮','section':'人事部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00012','name':'黄柏仪','section':'宣传部','position':'员工','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00013','name':'夏雅惠','section':'运营部','position':'员工','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00014','name':'梁哲宇','section':'开发部','position':'主管','sex':'男','edu':'硕士','birthday':'1978-04-21','entry':'2010-07-01'},
    {'id':'D00015','name':'叶洁启','section':'财务部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00016','name':'周孟儒','section':'开发部','position':'员工','sex':'男','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00017','name':'陈淑妤','section':'人事部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00018','name':'黄育霖','section':'宣传部','position':'员工','sex':'男','edu':'硕士','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00019','name':'金雅琪','section':'运营部','position':'员工','sex':'女','edu':'本科','birthday':'1983-11-04','entry':'2010-07-01'},
    {'id':'D00020','name':'叶洁启','section':'策划部','position':'主管','sex':'男','edu':'本科','birthday':'1993-11-04','entry':'2016-07-01'}]

def info(request):
    section = request.GET.get('section')
    position = request.GET.get('position')
    id = request.GET.get('id')
    name = request.GET.get('name')
    
    thisList = []
    
    for staff in staffList:
        if section:
            if staff['section']!= section:
                continue
        else:
            section = ""  
               
        if position:
            if staff['position']!= position:
                continue
        else:
            position = "" 
        
        if id:
            if staff['id']!= id:
                continue
        else:
            id = ""
           
        if name:
            if staff['name']!= name:
                continue
        else:
            name = ""
        
        thisList.append(staff) 
      
    context = {
        'staffList':thisList,
        'section':section,
        'position':position,
        'id':id,
        'name':name
    } 
                    
    return render(request, "polls/info.html", context)

# 详细信息页面设定
def detail(request, id):
    detailInfo = {}
    for staff in staffList:
        if staff['id'] == id:
            detailInfo = staff
    context={
        'staff':detailInfo,
    }
    return render(request, "polls/detail.html",context)