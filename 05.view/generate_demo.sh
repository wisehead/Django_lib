#############################################################
#   File Name: generate_demo.sh
#     Autohor: Hui Chen (c) 2022
#        Mail: alex.chenhui@gmail.com
# Create Time: 2022/03/09-08:55:20
#############################################################
#!/bin/sh 
django-admin startproject HelloWorld
django-admin startapp TestModel
#create table
python3 manage.py migrate   # 创建表结构

python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate TestModel   # 创建表结构
