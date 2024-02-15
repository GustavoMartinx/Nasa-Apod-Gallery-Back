from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from rest_framework import status

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
