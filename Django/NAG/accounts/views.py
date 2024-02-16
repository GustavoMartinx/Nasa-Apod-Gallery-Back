from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework import status

from allauth.socialaccount.models import SocialAccount

@login_required
def get_user_profile(request):
    user = request.user
    social_account = SocialAccount.objects.filter(user=user).first()
    
    if social_account:
        user_data = {
            'username': user.username,
            'name': social_account.extra_data.get('name', ''),
            'picture': social_account.extra_data.get('picture', ''),
        }
        return JsonResponse(user_data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Social account not found'}, status=status.HTTP_400_BAD_REQUEST)
