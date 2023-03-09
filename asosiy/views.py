from django.db.models import Sum,Avg
from django.shortcuts import render, redirect
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
        izohlar=Izoh.objects.filter(mahsulot_fk__id=son)

        urtacha_izoh=izohlar.aggregate(Avg('baho')).get('baho__avg')
        if urtacha_izoh:
            urtacha_izoh*=20
        else:
            urtacha_izoh=0
        data={
            "data":Mahsulot.objects.get(id=son),
            'media':Media.objects.filter(bolim_fk__id=son),
            'izohlar':izohlar,
            'izohlar_soni':Izoh.objects.filter(mahsulot_fk__id=son).count(),
            'urtacha_izohlar':urtacha_izoh
        }
        return render(request,'page-detail-product.html',data)
    def post(self,request,son):
        Izoh.objects.create(
            baho=request.POST.get('rating'),
            matn=request.POST.get('comment'),
            mahsulot_fk=Mahsulot.objects.get(id=son),
            profil_fk=Profil.objects.get(user=request.user)
        )
        return redirect(f'/asosiy/mahsulot/{son}')

