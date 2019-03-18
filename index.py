# import math
# name = input("input is name:")
# print("hello,world!","my name is "+name,"happy new yeah.")
# print('''中文skr''')
# print(chr(87),ord("中"))
# print("中文".encode('utf-8'))
# print(b'ddddddd')
# str="hi, %s .happy %d years!" % ("kang",2019)
# str= "hello,{0} 成绩提升了 {1:.2f}%".format("kang",17.123)
# print(str)
# classmetes = ['Micha','bob','tracy']
# print(len(classmetes))
# print(classmetes[-1])
# tu = (3,[111,222])
# print(tu[0],tu[1][1])
# height =input('输入你的身高cm：')
# weight =input('输入你的体重kg')
# value = float(weight)/math.pow(float(height)/100,2)
# print("BMI:{0:.2f}".format(value))
# if value < 18.5:
#     print("过瘦")
# elif value < 25:
#     print("正常")
# elif value < 28:
#     print("过重")
# elif value < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# for i in [1,2,4,5,6]:
#     print(i)

#dict
# dict = {'a':1,'b':2}
# print(dict.get('c',3))

# 可变参数
# def calc(*number):
#     sum = 0
#     for n in number:
#         sum = sum + n*n  
#     return sum   
# print(calc(1,2))

# 关键字参数
# def person(name,age,*params,city,job):
#     print(name,age,city,job)

# print('namsss',29,city="xm",job="it")
    
#高级特性
#切片 L[起始:为止:间隔]
# L = ['1','2','3','4']
# print(L[1:3])
#迭代
#列表生成式
#生成器
#迭代器

#函数式编程
#高阶函数
#map/reduce
# def f(x):
#     return x*x
# print(list(map(f,[1,2,3,4,5])))
# print(list(map(str,[1,2,3,4,5])))

#reduce 必须接收两个参数,且结果累积
# from functools import reduce
# def add(x,y):
#     return x*y
# print(reduce(add,[1,2,3,4,5]))

#filter过滤序列,返回true保留
# def is_odd(n):
#     return n %2 ==1
# print(list(filter(is_odd,[1,2,3,4,5,6,7])))

#sorted排序算法,key=str.lower 忽略大小写;reverse=True反向排序
# a = sorted(['ab','dc','Da'],key=str.lower,reverse=True)
# print(a)

#返回函数
# def layzy_sum(x,y):
#     def sum():
#         return x*y
#     return sum
# f = layzy_sum(2,5)
# print(f())

#匿名函数lambda
# f = lambda x:x*x
# print(f(2))

#装饰器
def log(func): 
    def wrapper(*args,**kw):
        print('log inster ...')
        return func(*args,**kw)
    return wrapper
@log
def now(x):
    print('2019.02.15'+x)

now('ddd')
#数字加密
# import random

# device = random.randint(1000000000,9999999999);
# time = 1548073809;
# pwd = 123456;
# devlist = tuple(str(device))
# print(devlist)
# timelist = list(str(time))
# timelist[0] = str(random.randint(0,9))
# timelist[9] = str(random.randint(0,9))

# #位移
# tmp = '';
# tmp2 = '';
# for idx in devlist:
#     if tmp == '':
#         tmp = timelist[int(idx)]
#     else:
#         tmp2 = timelist[int(idx)]
#         timelist[int(idx)] = tmp
#         tmp = tmp2
# print(timelist)    
# #与密码栅栏加密


 








