
from django.urls import path ,include

from .views import *
urlpatterns = [
path('savat/',SavatView.as_view()),
path('buyurtma/',BuyurtmaView.as_view()),
path('tanlangan/',TanlanganView.as_view()),
path('miqdorqosh/<int:son>/',MiqdorQoshView.as_view()),
path('miqdorkam/<int:son>/',MiqdorKamView.as_view()),
path('tanlanganqosh/<int:son>/',TanlanganQosh.as_view()),
path('savatqosh/<int:son>/',SavatQosh.as_view()),
path('savatuchir/<int:son>/',SavatUchir.as_view()),
path('tanlanganuchir/<int:son>/',TanlanganUchir.as_view()),

]
