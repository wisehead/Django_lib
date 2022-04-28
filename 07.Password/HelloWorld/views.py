from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
 
def hello(request):
    password = 'Admin123;'
    print('password:', password)
    ss = make_password(password)
    print('password:', ss)
    ret = check_password(password, ss)
    print('ret', ret)
    return HttpResponse("Hello world ! ")
