from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='index'), #home
    path('about', views.portfolio, name='about'), #portfolio
    path('contact', views.contact, name='contact'), #contact
]
