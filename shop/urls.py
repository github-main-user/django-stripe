from django.urls import path

from . import views
from .apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path("item/<int:pk>/", views.item_page, name="item-page"),
    path(
        "buy/<int:pk>/", views.create_checkout_session, name="create-checkout-session"
    ),
]
