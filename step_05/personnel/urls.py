from django.urls import path
from . import views,tests

urlpatterns = [
    path("", views.index),                       # index页面（http://127.0.0.1:8000/personnel/）
    
    # STEP05成果物页面
    path("info/", views.info),                   # 员工信息查询页面（http://127.0.0.1:8000/personnel/info/）
    path("info/detail/<str:id>", views.detail),  # 员工详细信息页面（http://127.0.0.1:8000/personnel/info/detail/Dxxxxx）
    
    # django 连接数据库增删改查练习
    path("insertdb/",tests.insertdb),            # 后台插入数据   （http://127.0.0.1:8000/personnel/insertdb/）
    path("updatedb/",tests.updatedb),            # 后台更新数据   （http://127.0.0.1:8000/personnel/updatedb/）
    path("deletedb/",tests.deletedb),            # 后台删除数据   （http://127.0.0.1:8000/personnel/deletedb/）
    path("selectdb/",tests.selectdb),            # 后台删除数据   （http://127.0.0.1:8000/personnel/selectdb/）
]