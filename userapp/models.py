from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    ism=models.CharField(max_length=25)
    jins=models.CharField(max_length=5)
    shaxar=models.CharField(max_length=50)
    davlat=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.ism
