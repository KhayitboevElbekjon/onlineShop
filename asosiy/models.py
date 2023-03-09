from django.db import models

from userapp.models import Profil


class Bolim(models.Model):
    nom=models.CharField(max_length=100)
    rasm=models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom
class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    narx=models.IntegerField()
    brend=models.CharField(max_length=50)
    davlat=models.CharField(max_length=50)
    kafolat=models.CharField(max_length=50)
    bolim_fk=models.ForeignKey(Bolim,on_delete=models.CASCADE)
    min_miqdor=models.SmallIntegerField(default=1)
    tasdiqlangan=models.BooleanField(default=True)
    yetkazish=models.CharField(max_length=25)
    mavjud=models.BooleanField(default=True)
    chegirma=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.nom},{self.brend}"
class Media(models.Model):
    rasm=models.FileField(upload_to='mahsulotlar')
    bolim_fk = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Izoh(models.Model):
    baho=models.SmallIntegerField()
    matn=models.TextField()
    sana=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    mahsulot_fk=models.ForeignKey(Mahsulot,on_delete=models.CASCADE,null=True)
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
