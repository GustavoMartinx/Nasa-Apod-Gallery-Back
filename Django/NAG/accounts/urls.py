from django.urls import path
from . import views

# users/
urlpatterns = [
    path('profile/', views.get_user_profile),
]
