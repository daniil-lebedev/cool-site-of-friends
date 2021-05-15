from django.urls import path

from . import views 

urlpatterns = [
    #path for tan
    path('', views.TanPage, name = "TanPage" ),


]
