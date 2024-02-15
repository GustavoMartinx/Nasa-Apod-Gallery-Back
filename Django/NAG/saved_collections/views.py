from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.models import SocialAccount
from .models import SavedCollections
from django.http import JsonResponse
from rest_framework import status
import json

@csrf_exempt
# @login_required
def create_new_collection(request):

    if request.method == 'POST':
        # Decodifica o corpo da requisição para um dicionário Python
        request_data = json.loads(request.body.decode('utf-8'))

        collectionName = request_data.get('collection_name')
        # dateList = request_data.get('date_list')
        username = request_data.get('user')
        
        # print("username", username)
        # print("collectionName", collectionName)
        
        try:
            SavedCollections.objects.create(
                name = collectionName,
                # date_list = dateList,
                user = username,
            )
        except:
            return JsonResponse({'error': 'Something went wrong while creating the collection'}, status=status.HTTP_400_BAD_REQUEST)
        
        return JsonResponse({'message': f'Collection {collectionName} created successfully!'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
