from django.urls import path
from . import views

urlpatterns = [
    path('', views.Movie, name='index'),
    path('filldata/', views.filldetails),
    path('savedata/', views.InsertData, name='savedata')
]