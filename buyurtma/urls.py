
from django.urls import path ,include

from .views import *
urlpatterns = [
path('savat/',SavatView.as_view()),
path('buyurtma/',BuyurtmaView.as_view()),
path('tanlangan/',TanlanganView.as_view()),

]
