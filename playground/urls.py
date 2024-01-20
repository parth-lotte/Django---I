#  Mapping urls 

from django.urls import path 
from . import views 

urlpatterns= [
    
    
    #URL Config
    #  array of url pattern object
    path('hello/', views.say_hello)
]