# coding=utf-8
import datetime

id = input("请输入您的身份证号码")

# 提取性别信息 （身份证第17位为性别）
sex = "先生" if int(id[16:17]) % 2 else "女士"

# 提取省份信息 （身份证第1～2位为省份）

add = {'11':'北京','12':'天津','13':'河北','14':'山西','15':'内蒙',
       '21':'辽宁','22':'吉林','23':'黑龙江','31':'上海','32':'江苏',
       '33':'浙江','34':'安徽','35':'福建','36':'江西','37':'山东',
       '41':'河北','42':'湖北','43':'湖南','44':'广东','45':'广西',
       '46':'海南','50':'重庆','51':'四川','52':'贵州','53':'云南',
       '54':'西藏','61':'陕西','62':'甘肃','63':'青海','64':'宁夏',
       '65':'新疆','71':'台湾','81':'香港'}
myadd = add[id[0:2]]

# 提取出生日期 （身份证第7～14位为性别）
year = int(id[6:10])
month = int(id[10:12])
day = int(id[12:14])

# 提取年龄
today = datetime.date.today()
age = today.year - year - ((today.month,today.day) < (month,day))

# 提取生肖
sx = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
mysx = sx[year % 12]

# 提取星座
xz =('摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座') 
d = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
myxz = xz[len(list(filter(lambda y:y<(month,day),d)))]

# 输出相关信息
print(f"{sex}您好，您来自{myadd},出生于{year}年{month}月{day}日,属{mysx},{myxz}，满{age}周岁啦！")
