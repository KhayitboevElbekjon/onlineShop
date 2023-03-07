

from django.urls import path,include

from .views import *
urlpatterns = [
    path('category/',BolimlarView.as_view()),
    path('home/',HomeView.as_view()),
    path('bolim/<int:son>/',BittaBolimView.as_view()),
    path('mahsulot/<int:son>/',BittaMahsulotView.as_view()),
]
