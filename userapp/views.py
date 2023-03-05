from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout


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

        return redirect('/userapp/')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/userapp/')

class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')