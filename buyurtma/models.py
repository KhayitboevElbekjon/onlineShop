from django.db import models

from asosiy.models import Mahsulot
from userapp.models import Profil
class Savat(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot_fk=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdori=models.SmallIntegerField()
    narxi=models.IntegerField()


class Tanlangan(models.Model):
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot_fk=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)