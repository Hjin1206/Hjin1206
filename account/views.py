from django.shortcuts import render,HttpResponse,redirect
from account.models import User

# Create your views here.
def regist(request):
    return render(request,"regist.html")

def registlogic(request):
    name = request.POST.get("username")
    pwd = request.POST.get("userpwd")
    u = User.objects.create(name=name,password=pwd)
    if u:
        return redirect("/account/login/")
    return HttpResponse("注册失败")

def login(request):
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('pwd')
    result = User.objects.filter(name=name,password=pwd)
    if result:
        request.session['login'] = 1
        return redirect("/account/home/")
    return render(request,"login.html")

def loginlogic(request):
    name = request.POST.get("username")
    pwd = request.POST.get("userpwd")
    rem = request.POST.get('remember')
    result = User.objects.filter(name=name,password=pwd)
    if result:
        response = redirect("/account/home/")
        request.session['login'] = 1
        if rem:
            response.set_cookie("name",name,max_age=7*24*36000)
            response.set_cookie("pwd",pwd,max_age=7*24*36000)
        return response
    return HttpResponse("登录失败")




def home(request):
    status = request.session.get('login')
    if status:
        return render(request,'home.html')
    return redirect('acount/login/')
