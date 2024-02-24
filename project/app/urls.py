from django.urls import path
from .views import neha,app_01



urlpatterns = [
     path('',app_01 ),
    path('neha/',neha,name='savedata' ),
       
]

