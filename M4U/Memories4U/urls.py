from django.urls import path
from Memories4U import views #from . import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="at"),
    path('cnt/',views.contact,name="ct"),
    
    path('events/',views.events,name="events"), 
    path('gallary/',views.gallary,name="gallary"),
    
]