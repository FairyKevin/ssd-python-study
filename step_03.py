#!/usr/bin/python3
# coding=utf-8

import pymysql
import datetime

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=8889,
                     user='root',
                     password='root',
                     database='python_study')
# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()


# 创建数据库表
# 如果表存在则删除：DROP TABLE IF EXISTS 表名
cursor.execute("DROP TABLE IF EXISTS employee")
    
# 创建表：CREATE TABLE 表名(字段名 字段类型)
sql_todo = """CREATE TABLE employee(
    id CHAR(6) NOT NULL UNIQUE,
    name CHAR(10) NOT NULL,
    department CHAR(10),
    sex CHAR(1),
    birthday DATE,
    income FLOAT,
    primary key(id))"""
    
cursor.execute(sql_todo) 
print("员工表创建完成\n")


# 单条数据插入
sql_todo = """INSERT INTO employee(
    id,name,department,sex,birthday,income)
    VALUES('D00001','张吉惟','开发部','男','1988-12-01',11000)"""

try:
    # 执行数据插入命令
    cursor.execute(sql_todo)     
    # 提交到数据库执行
    db.commit() 
    print(cursor.rowcount,"条数据已插入\n")
except:
    # 如果发生错误则回滚
    db.rollback()
    print("¡¡¡单条数据插入失败\n")
    

# 多条数据插入
sql = """INSERT INTO employee (
    id,name,department,sex,birthday,income) 
    VALUES (%s,%s,%s,%s,%s,%s)"""
    
val=[
    ('D00002','林国瑞','开发部','男','1976-10-20',15000),
    ('D00003','刘姿婷','企划部','女','1992-06-14',9000),
    ('D00004','夏志豪','企划部','男','1983-08-01',13000),
    ('D00005','郑伊雯','企划部','女','1990-03-20',8000),
    ('D00006','林玟书','开发部','女','1980-03-20',14000),
    ('D00007','江奕云','企划部','男','1992-03-20',9800),
    ('D00008','刘柏宏','开发部','男','1984-03-20',13000),
    ('D00009','阮建安','开发部','男','1982-03-20',14000),
    ('D00010','林子帆','开发部','女','1996-03-20',6500)
    ]

try:
    # 执行数据插入命令
    cursor.executemany(sql,val)     
    # 提交到数据库执行
    db.commit() 
    print(cursor.rowcount,"条数据已插入\n")
except:
    # 如果发生错误则回滚
    db.rollback()
    print("¡¡¡多条数据插入失败\n")



# 数据更新
sql_todo = """UPDATE employee SET department = "企划部" WHERE name = '张吉惟'"""

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)     
    # 提交到数据库执行
    db.commit() 
    print(cursor.rowcount,"条数据被更新\n")
except:
    # 如果发生错误则回滚
    db.rollback()
    print("¡¡¡数据更新失败\n")    


# 数据删除
sql_todo = """DELETE FROM employee WHERE name = '夏志豪'"""

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)     
    # 提交到数据库执行
    db.commit() 
    print(cursor.rowcount,"条数据被删除\n")
except:
    # 如果发生错误则回滚
    db.rollback()
    print("¡¡¡数据删除失败\n") 

# 查询数据
sql_todo = "SELECT * FROM employee"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表 (获取单条数据：fetchone()、获取所有数据：etchall()、获取n条数据：fetchmany(n))
    results = cursor.fetchall()  
    print("查询1：获取员工表所有信息，结果如下：")
    # 提取所需信息
    for row in results:
        print(row)
except:
   print("¡¡¡查询1 失败")   
   
print()
   
   
# 指定条件查询：WHERE ～ ；模糊查询：LIKE（%）
sql_todo = "SELECT * FROM employee WHERE name LIKE '刘%'"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表
    results = cursor.fetchall()  
    print("查询2：获取刘姓员工信息，结果如下：")
    # 提取所需信息
    for row in results:
        print(row)
except:
   print("¡¡¡查询2 失败")   
   
print()


# 查询结果排序:ORDER BY ，默认升序，关键字 ASC，如果要降序需设置关键字 DESC。
sql_todo = "SELECT name,income FROM employee WHERE income > 10000 ORDER BY income DESC"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表
    results = cursor.fetchall()  
    print("查询3：月收入高于1万的员工有：")
    # 提取所需信息
    for row in results:
        name = row[0]
        income = row[1]
        # 打印结果
        print("・%s 收入：%s元" % (name,income))
except:
   print("¡¡¡查询3 失败") 
   
print()   


# 设置查询的数据量，可以通过 "LIMIT" 语句来指定
sql_todo = "SELECT name,income FROM employee ORDER BY income DESC LIMIT 3"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表
    results = cursor.fetchall()  
    print("查询4：月收入排名前三的员工为：")
    # 提取所需信息
    for row in results:
        name = row[0]
        income = row[1]
        # 打印结果
        print("・%s 收入：%s元" % (name,income))
except:
   print("¡¡¡查询4 失败") 
   
print()


# 指定起始位置，使用的关键字是 OFFSET  （ 0 为 第一条，1 为第二条，以此类推 ）
sql_todo = "SELECT name,income FROM employee ORDER BY income DESC LIMIT 3 OFFSET 3"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表
    results = cursor.fetchall()  
    print("查询5：月收入排名第四～六名的员工为：")
    # 提取所需信息
    for row in results:
        name = row[0]
        income = row[1]
        # 打印结果
        print("・%s 收入：%s元" % (name,income))
except:
   print("¡¡¡查询5 失败")  
   
print()
   

# 多表查询：SELECT * FROM 表1 LEFT JOIN 表2 ON 表1.id = 表2.id WHERE ～  
sql_todo = "SELECT employee.name,employee.department,department.leader FROM employee LEFT JOIN department ON employee.department = department.name"

try:
    # 执行数据更新命令
    cursor.execute(sql_todo)   
    # 获取所有记录列表
    results = cursor.fetchall()  
    print("查询6：员工所在部门及部门负责人情况如下：")
    # 提取所需信息
    for row in results:
        name = row[0]
        department = row[1]
        leader = row[2]
        # 打印结果
        print("・员工：%s %s 负责人为：%s " % (name,department,leader))
except:
   print("¡¡¡查询6 失败") 
   
print()   
 
# 关闭数据库连接
db.close()

exit()