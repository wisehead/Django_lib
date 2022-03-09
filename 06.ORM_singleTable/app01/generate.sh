#############################################################
#   File Name: generate.sh
#     Autohor: Hui Chen (c) 2022
#        Mail: alex.chenhui@gmail.com
# Create Time: 2022/03/09-15:16:45
#############################################################
#!/bin/sh 
python3 manage.py migrate   # 创建表结构
python3 manage.py makemigrations app01  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate app01   # 创建表结构
