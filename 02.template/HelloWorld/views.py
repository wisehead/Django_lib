from django.http import HttpResponse
from django.shortcuts import render

"""
def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)
"""

"""
def runoob(request):
  views_name = "菜鸟教程"
  return  render(request,"runoob.html", {"name":views_name})
"""
"""
def runoob(request):
    views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request, "runoob.html", {"views_list": views_list})
"""

"""
def runoob(request):
    views_dict = {"name":"菜鸟教程"}
    return render(request, "runoob.html", {"views_dict": views_dict})
"""

def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    return render(request, "runoob.html", {"views_list": views_list})

def hello(request):
    return HttpResponse("Hello world ! ")
