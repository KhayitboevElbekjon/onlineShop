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
class BolimlarView(View):
    def get(self,request):
        data={
            'data':Bolim.objects.all()
        }
        return render(request,'page-category.html',data)

class BittaBolimView(View):
    def get(self,request,son):
        B=Bolim.objects.get(id=son)
        data={
            'data':Mahsulot.objects.filter(bolim_fk=B)
        }
        return render(request,'page-listing-grid.html',data)

class BittaMahsulotView(View):
    def get(self,request,son):
        data={
            "data":Mahsulot.objects.get(id=son),
            'media':Media.objects.filter(bolim_fk__id=son)
        }
        return render(request,'page-detail-product.html',data)