from django.urls import path
from . import views


# из этого директория . беру файл views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', views.register, name='register')
]
