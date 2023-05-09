from django.contrib import admin
from django.urls import path
from internship import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('bitcoin_price/', views.get_bitcoin_price, name='bitcoin_price'),
]
