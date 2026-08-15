from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_shortlink, name='create'),
    path('<str:slug>', views.redirect_to_original, name='redirect'),
]