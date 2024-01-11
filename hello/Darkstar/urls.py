
from django.contrib import admin
from django.urls import path,include
from Darkstar import views
urlpatterns = [
    path("",views.index,name="Home"),
    path("about",views.about,name="About"),
    path("contact",views.contact,name="contact"),
    path("services",views.services,name="services"),
    
]
