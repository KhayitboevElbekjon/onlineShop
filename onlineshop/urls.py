
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('', include('userapp.urls')),


    path('Page_index_2', Home2View.as_view())



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
