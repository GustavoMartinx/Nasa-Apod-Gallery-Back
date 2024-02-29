from django.urls import path
from . import views

# saved-collections/
urlpatterns = [
    path('create/', views.create_new_collection),
    path('list/', views.list_saved_collections),
    path('rename/', views.rename_collection),
    path('delete/<str:collection_name>/', views.delete_collection, name='delete_collection'),

    path('add-image/', views.add_image_to_collection),
]
