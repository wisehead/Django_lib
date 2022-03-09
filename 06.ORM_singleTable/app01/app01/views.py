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

def add_book(request):
    books = models.Book.objects.all()
    #print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功！</p>")

"""
def add_book(request):
    books = models.Book.objects.filter(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！</p>")
"""
