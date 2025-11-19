from django.urls import path

from .apps import ShopConfig
from .views import home

app_name = ShopConfig.name

urlpatterns = [
    path("", home, name="home"),
]
