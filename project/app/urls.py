from django.urls import path
from .views import neha,app_01



urlpatterns = [
     path('app',app_01,name='neha' ),
    path('',neha,name='neha' ),
       
]

