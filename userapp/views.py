from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout

from .models import Profil


class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')
    def post(self,request):
        loginn=request.POST.get('loginn')
        paroll=request.POST.get('paroll')
        user=authenticate(request,password=paroll,username=loginn)
        if user is not  None:
            login(request, user)
            return redirect('/asosiy/home/')

        return redirect('/register')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')
    def post(self,request):
        name=request.POST.get('ism')
        pp=request.POST.get('parol')
        tp=request.POST.get('takparol')
        shaxaR=request.POST.get('shaxar')
        davlaT=request.POST.get('davlat')
        jins=request.POST.get('jins')
        email=request.POST.get('email')
        if pp == tp:
            user1=User.objects.create_user(username=email,password=tp)
            Profil.objects.create(
                ism=name,
                jins=jins,
                shaxar=shaxaR,
                davlat=davlaT,
                user=user1
            )
            return redirect('/')

