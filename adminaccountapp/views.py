from django.shortcuts import render,redirect,HttpResponse
from .models import UserInfo,UserForm,LoginForm
from django.contrib.auth import login,logout,authenticate
#from customersapp.models import Customersapp   
#from servicapp.models import Servicapp 
#from appointmentapp.models import Appointmentapp   
from django.contrib.auth.models import User

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        context={'form':f}
        if f.is_valid():
            f.save()
            return redirect('/')
        else:
            return render(request,'register.html',context)        
    else:
        f=UserForm()
        context={'form':f}
        return render(request,"register.html",context)


def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')  
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            #request.session["uid"]=user.id 
            login(request,user)
            return redirect('/')
        else:
            #context={'msg':"userName And Password is Not Valid"} 
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def edit_profile(request):
    uid = request.session.get('uid')
    user = UserInfo.objects.filter(user_ptr=uid).first()
    if request.method=='POST':
        u=UserForm(request.POST,instance=request.user)
        context={'form':u}
        if u.is_valid():
            u.save()
            return redirect('/')
        else:
            return render(request,"update_account.html",context)
    else:
        f=UserForm(instance=request.user)
        context={'form':f}
        return render(request,"update_account.html",context)

#tuple, list differnc tuple , class list comparasion , 
#django: models,  

def about_us(request):
    return render(request,'aboutus.html')