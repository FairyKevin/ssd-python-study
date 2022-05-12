from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from personnel.models import Staff


# 插入数据
def insertdb(requst):
    
    # 单条插入 方法一       主键存在的情况下，可直接更新
    data1 = Staff(id='D00001',name='张吉惟',section='开发部',position='员工',sex='男',edu='本科',birthday='1985-11-04',entry='2018-07-01')
    data1.save()
    
    # 单条插入 方法二       主键存在的情况下，不能再插入
    # data2 = Staff.objects.create(id='D00002',name='林国瑞',section='开发部',position='主管',sex='男',edu='硕士',birthday='1978-04-21',entry='2010-07-01')
    
    # 批量插入 bulk_create      主键存在的情况下，不能再插入
    data_list =[
        Staff(id='D00025',name='周白芷',section='开发部',position='员工',sex='女',edu='本科',birthday='1983-06-04',entry='2021-07-01'),
        Staff(id='D00026',name='黄盛玫',section='人事部',position='员工',sex='女',edu='本科',birthday='1983-09-04',entry='2015-08-01'),
        Staff(id='D00027',name='张孟涵',section='宣传部',position='员工',sex='女',edu='硕士',birthday='1990-01-18',entry='2019-07-01'),
        Staff(id='D00028',name='许智云',section='运营部',position='员工',sex='男',edu='本科',birthday='1976-07-04',entry='2020-10-01'),
        Staff(id='D00029',name='卢木仲',section='开发部',position='员工',sex='男',edu='本科',birthday='1979-09-14',entry='2016-07-01'),
        Staff(id='D00030',name='吴美隆',section='财务部',position='员工',sex='男',edu='本科',birthday='1991-11-20',entry='2014-09-01'),
        Staff(id='D00031',name='谢彦文',section='开发部',position='员工',sex='男',edu='硕士',birthday='1989-05-24',entry='2019-07-01'),
        Staff(id='D00032',name='吉茹定',section='人事部',position='员工',sex='男',edu='硕士',birthday='1983-07-23',entry='2017-04-01'),
        Staff(id='D00033',name='黄芸欢',section='宣传部',position='员工',sex='女',edu='本科',birthday='1990-02-10',entry='2016-07-01'),
        Staff(id='D00034',name='刘翊惠',section='运营部',position='员工',sex='女',edu='本科',birthday='1983-05-04',entry='2019-11-01'),   
    ]
    
    Staff.objects.bulk_create(data_list)  
    return HttpResponse("<p>数据添加成功！</p>")


# 删除数据
def deletedb(request):
    
    # 删除数据 方法一
    deldate1 = Staff.objects.get(id='D00014')
    deldate1.delete()
    
    # 删除数据 方法二
    Staff.objects.filter(id='D00013').delete()
    
    # 删除所有数据
    # Staff.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")



# 更新数据
def updatedb(request):
    
    # 更新数据 方法一
    update1 = Staff.objects.get(id='D00001')
    update1.section = '运营部'
    update1.save()
    
    # 更新数据 方法二
    Staff.objects.filter(id='D00003').update(section='开发部')
    
    # 更新所有的列
    # Staff.objects.all().update(section='开发部')
    
    return HttpResponse("<p>修改成功</p>")
    
    

# 获取数据
def selectdb(request):
    
    # 初始化
    select1 = ""
    select2 = ""
    
    # 返回查询集
    # all() 获取所有数据，对应SQL：select * from Staff
    list1 = Staff.objects.all()
    
    # filter 相当于 SQL 中的 WHERE，可设置过滤条件
    list2 = Staff.objects.filter()
    list3 = Staff.objects.filter(sex='女')
    list4 = Staff.objects.filter(sex='女',section='开发部')
    list4 = Staff.objects.filter(sex='女').filter(section='开发部')
    
    # exclude 不匹配
    list5 = Staff.objects.exclude(sex='女')
    
    # order_by 数据排序 默认是升序;降序在字段名前加’-’
    list6 = Staff.objects.order_by("section")
    list7 = Staff.objects.order_by("-section")
    list8 = Staff.objects.order_by("-section","sex")
    
    # 查询集限制
    # 查询集类似列表，可以使用下标进行限制，类似sql语句中的limit子句。但索引不能是负数
    Staff.objects.all()[0]      #等同于：limit 0,1
    Staff.objects.all()[2]      #等同于：limit 2,1
    Staff.objects.all()[0:2]    #等同于limit 2
    Staff.objects.all()[:2]     #等同于limit 2
    Staff.objects.all()[::2]
    
    # 上面方法可以连锁使用
    select2 = Staff.objects.filter(sex='女').order_by("section")
    
    
    # 返回单个值
    # get() 只匹配一条数据
    data1 = Staff.objects.get(id='D00001')
    
    # first()和last()
    data2 = Staff.objects.all().first()
    data3 = Staff.objects.all().last()
    
    # count()
    data4 = Staff.objects.count()
    
    # exists()
    data5 = Staff.objects.filter(id='D00001').exists()
    

    # 输出所有数据
    for data in list3:
        select1 += data.name + " "
    select2 = select1
    return HttpResponse("<p>"+ select2 + "</p>")
    