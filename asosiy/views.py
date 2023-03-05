from django.shortcuts import render
from django.views import View
from .models import *
class Home2View(View):
    def get(self,request):
        return render(request,'page-index-2.html')

class HomeView(View):
    def get(self,request):
        data={
            'data':Bolim.objects.all()[:7],
            'chegirmalilar':Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]
        }
        return render(request,'page-index.html',data)

