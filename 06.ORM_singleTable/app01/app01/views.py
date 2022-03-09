from django.shortcuts import render,HttpResponse
from app01 import models 

"""
def add_book(request):
    book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8") 
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    print(books, type(books)) # Book object (18)
    return HttpResponse("<p>数据添加成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.all()
    #print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.filter(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")

def add_book(request):
    books = models.Book.objects.exclude(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")

def add_book(request):
    books = models.Book.objects.get(pk=1)
    #books = models.Book.objects.get(pk=18)  # 报错，没有符合条件的对象
    #books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    print(books, type(books))  # 模型类的对象
    print(books.title)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.order_by("price") # 查询所有，按照价格升序排列
    for i in books:
        print(i.title)
    books = models.Book.objects.order_by("-price") # 查询所有，按照价格降序排列
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    # 按照价格升序排列：降序再反转
    books = models.Book.objects.order_by("-price").reverse()
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.count() # 查询所有数据的数量
    books = models.Book.objects.filter(price=200).count() # 查询符合条件数据的数量
    print (books)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.first() # 返回所有数据的第一条数据
    print (books)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.last() # 返回所有数据的最后一条数据
    print (books)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    books = models.Book.objects.exists()
    print (books)
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    #books = models.Book.objects.count().exists()
    print (books)
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    #books = models.Book.objects.first().exists()
    print (books)
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    # 查询所有的id字段和price字段的数据
    books = models.Book.objects.values("pk","price")
    print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！</p>")
"""

"""
def add_book(request):
    # 查询所有的price字段和publish字段的数据
    books = models.Book.objects.values_list("price","publish")
    print(books)
    print(books[0][0],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！</p>")
"""

from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    # 查询一共有多少个出版社
    books = models.Book.objects.values_list("publish").distinct() # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    print(books)
    books = models.Book.objects.distinct()
    print(books)
    return HttpResponse("<p>查找成功！</p>")
