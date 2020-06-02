from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:site_user>/', views.show_profile, name='show_profile_url'),
]