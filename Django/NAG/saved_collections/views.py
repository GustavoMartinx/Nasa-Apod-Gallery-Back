from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework import status

from .models import SavedCollections

# @csrf_exempt
@login_required
@api_view(['POST'])
def create_new_collection(request):

    request_data = request.data
    collectionName = request_data.get('collection_name')
    
    try:
        collection = SavedCollections.objects.get(name=collectionName, user=request.user)
        return JsonResponse({'error': f'Collection {collectionName} already exists. Please choose a different name.'}, status=status.HTTP_400_BAD_REQUEST)
    except SavedCollections.DoesNotExist:
        pass
    
    try:
        SavedCollections.objects.create(
            name = collectionName,
            user = request.user,
        )
    except:
        return JsonResponse({'error': 'Something went wrong while creating the collection.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'message': f'Collection {collectionName} created successfully!'}, status=status.HTTP_201_CREATED)


@login_required
@api_view(['GET'])
def list_saved_collections(request):
    try:
        collections = SavedCollections.objects.filter(user=request.user)
    except SavedCollections.DoesNotExist:
        return JsonResponse({'error': 'No collections found.'}, status=status.HTTP_404_NOT_FOUND)
    
    return JsonResponse({'collections': [collection.name for collection in collections]}, status=status.HTTP_200_OK)


@login_required
@api_view(['PUT'])
def rename_collection(request):
    try:
        collection = SavedCollections.objects.get(user=request.user, name=request.data.get('current_collection_name'))
        collection.name = request.data.get('new_collection_name')
    except SavedCollections.DoesNotExist:
        return JsonResponse({'error': f'Collection {request.data.get("current_collection_name")} not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        collection.save()
    except:
        return JsonResponse({'error': f'Something went wrong while renaming the {request.data.get("current_collection_name")} collection.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'message': 'Collection renamed successfully!'}, status=status.HTTP_200_OK)


@login_required
@api_view(['DELETE'])
def delete_collection(request, collection_name):
    try:
        collection = SavedCollections.objects.get(user=request.user, name=collection_name)
    except SavedCollections.DoesNotExist:
        return JsonResponse({'error': f'Collection {collection_name} not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        collection.delete()
    except:
        return JsonResponse({'error': f'Something went wrong while deleting the {collection_name} collection.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'message': f'Collection {collection_name} deleted successfully!'}, status=status.HTTP_200_OK)
