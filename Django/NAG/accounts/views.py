from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

@login_required
def get_user_profile(request):
    user = request.user
    print("user:", request.user)

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



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def generate_token(request):

    # print("user:", request.user)
    user = request.user
    social_account = SocialAccount.objects.filter(user=user).first()
    if social_account:
        access_token = AccessToken.for_user(user)
        print("access_token:", str(access_token))
        return JsonResponse({'access_token': str(access_token)}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Social account not found'}, status=status.HTTP_400_BAD_REQUEST)
