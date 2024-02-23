from django.urls import path
from . import views

# saved-collections/
urlpatterns = [
    path('create/', views.create_new_collection),
    path('list/', views.list_saved_collections),
    path('rename/', views.rename_collection),
]
