"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 

from . import views,testdb,search

"""
urlpatterns = [
    path(r'^$', views.hello, name='hello'),
]
"""

urlpatterns = [
    path('hello/', views.hello),
    path('runoob/', views.runoob),
    path(r'', views.hello),
    path('testdb/', testdb.testdb),
    path('search-form', search.search_form),
    path('search', search.search),
]

