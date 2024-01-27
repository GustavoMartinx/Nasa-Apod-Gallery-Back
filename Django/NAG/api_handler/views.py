# Views is a request handler.

from rest_framework import status
from django.http import JsonResponse
import requests

def get_images(request):
    
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
