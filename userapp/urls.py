
from django.urls import path ,include

from .views import *
urlpatterns = [
    path('',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('register/',RegisterView.as_view()),
]
