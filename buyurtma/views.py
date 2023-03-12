from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import *
class SavatView(View):
    def get(self,request):
        savat=Savat.objects.filter(profil_fk__user=request.user)
        summa=savat.aggregate(Sum('narxi')).get('narxi__sum')
        chegirmalar=0
        for i in savat:
            chegirmalar+=i.miqdori*(i.mahsulot_fk.chegirma*i.mahsulot_fk.narx)/100
        data={
            'mahsulot':savat,
            'summa':summa,
            'chegirma':round(chegirmalar,2),
            'yakuniy':summa-round(chegirmalar,2)
        }
        return render(request,'page-shopping-cart.html',data)

class SavatQosh(View):
    def get(self,request,son):
        profil = Profil.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.get(id=son)
        miqdor=Mahsulot.objects.get(id=son).min_miqdor
        narx=Mahsulot.objects.get(id=son).narx
        if profil:
            Savat.objects.create(
                profil_fk=profil,
                mahsulot_fk=mahsulot,
                miqdori=miqdor,
                narxi=narx
            )
        return redirect('/buyurtma/savat/')
class SavatUchir(View):
    def get(self,request,son):
        savat = Savat.objects.get(id=son)
        if savat.profil_fk.user==request.user:
            savat.delete()
        return redirect('/buyurtma/savat/')
class BuyurtmaView(View):
    def get(self,request):
        return render(request,'page-profile-orders.html')

class TanlanganView(View):
    def get(self,request):
        data={
            'tanlanganlar':Tanlangan.objects.filter(profil_fk__user=request.user)
        }
        return render(request,'page-profile-wishlist.html',data)
class TanlanganQosh(View):
    def get(self,request,son):
        profil=Profil.objects.get(user=request.user)
        mahsulot=Mahsulot.objects.get(id=son)
        if profil:
            Tanlangan.objects.create(
                profil_fk=profil,
                mahsulot_fk=mahsulot
            )
        return redirect('/buyurtma/tanlangan')
class TanlanganUchir(View):
    def get(self,request,son):
        tanlangan=Tanlangan.objects.get(id=son)
        if tanlangan.profil_fk.user==request.user:
            tanlangan.delete()
        return redirect('/buyurtma/tanlangan')



class MiqdorQoshView(View):
    def get(self,request,son):
        nar=Savat.objects.get(id=son)
        if nar.profil_fk.user==request.user :
            nar.miqdori+=1
            nar.narxi+=nar.mahsulot_fk.narx
            nar.save()

        return redirect('/buyurtma/savat')

class MiqdorKamView(View):
    def get(self,request,son):
        nar=Savat.objects.get(id=son)
        if nar.profil_fk.user==request.user and nar.miqdori!=1:
            nar.miqdori-=1
            nar.narxi-=nar.mahsulot_fk.narx
            nar.save()

        return redirect('/buyurtma/savat/')