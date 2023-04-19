from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_location', views.send_location, name="send_location"),
    path('get_location', views.get_location, name="get_location"),
]