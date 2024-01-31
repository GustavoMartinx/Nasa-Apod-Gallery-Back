from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.get_images_unsplash_for_test),
    
    path('', views.get_images_nasa),
]