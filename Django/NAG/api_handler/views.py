# Views is a request handler.

from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
import requests

def get_images(request):
    
    # if (request.method == 'GET'):
    #     num_images = int(request.GET['num_images'])
    #     if (0 < num_images <= 9):

    #         url = 'https://source.unsplash.com/random'
    #         response = []

    #         for i in range(num_images):
    #             api_response = requests.get(url)

    #             # Check if the request was successful (status code 200)
    #             if api_response.status_code == 200:
    #                 response.append(api_response.content)
    #             else:
    #                 return JsonResponse({'error': f'Failed to fetch image {i}'}, status=status.HTTP_400_BAD_REQUEST)

    #         # send it back to frontend
    #         return JsonResponse({'images': response}, status=status.HTTP_200_OK)

    # return JsonResponse({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    # just to test
    return JsonResponse({'images': 'https://source.unsplash.com/random'}, status=status.HTTP_200_OK)