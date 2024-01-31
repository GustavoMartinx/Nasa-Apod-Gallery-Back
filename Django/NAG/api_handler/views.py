# Views is a request handler.

from rest_framework import status
from django.http import JsonResponse
from NAG.local_settings import API_KEY
import requests
import json

def get_images_unsplash_for_test(request):
    
    if (request.method == 'GET'):
        
        # getting the number of images to be fetched
        num_images = int(request.GET['num_images'])
        if (0 < num_images <= 9):

            url = 'https://source.unsplash.com/random'
            response = []

            # making the num_images as the number of requests
            for i in range(num_images):
                api_response = requests.get(url)

                if api_response.status_code == 200:
                    response.append(api_response.request.url)
                else:
                    return JsonResponse({'error': f'Failed to fetch image {i}'}, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse({'images_urls': response}, status=status.HTTP_200_OK)

    return JsonResponse({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


def get_images_nasa(request):

    if (request.method == 'GET'):
        
        # Getting the number of images to be fetched
        num_images = int(request.GET['num_images'])
        if (0 < num_images <= 9):

            url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count={num_images}'

            api_response = requests.get(url)

            if api_response.status_code == 200:
                json_response = json.loads(api_response.content.decode('utf-8'))
                return JsonResponse({'images_array': json_response}, status=status.HTTP_200_OK)
                
            else:
                return JsonResponse({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

