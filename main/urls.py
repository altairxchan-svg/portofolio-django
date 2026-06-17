from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('',          views.home,     name='home'),
    path('about/',    views.about,    name='about'),
    path('skills/',   views.skills,   name='skills'),
    path('services/', views.services, name='services'),
    path('blogs/',    views.blogs,    name='blogs'),
    path('contact/',  views.contact,  name='contact'),
    
]
