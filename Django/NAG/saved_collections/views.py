from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework import status

from .models import SavedCollections

@csrf_exempt
@login_required
@api_view(['POST'])
def create_new_collection(request):

    request_data = request.data
    collectionName = request_data.get('collection_name')
    
    try:
        SavedCollections.objects.create(
            name = collectionName,
            user = request.user,
        )
    except:
        return JsonResponse({'error': 'Something went wrong while creating the collection'}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'message': f'Collection {collectionName} created successfully!'}, status=status.HTTP_201_CREATED)
