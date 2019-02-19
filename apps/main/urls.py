from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shop$', views.shop),
    url(r'^services$', views.services),
]
