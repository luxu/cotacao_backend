from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('coins', views.request_in_site, name="list_coins")
]