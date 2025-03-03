from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
from.models import *
from.serializers import *

#create Accout
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    manual_parameters=[
        openapi.Parameter('username', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('password', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('first_name', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('last_name', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('phone_number', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('bio', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_account(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login Account
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    manual_parameters=[
        openapi.Parameter('username', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('password', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def login_account(request): 
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        # token, _ = Token.objects.get_or_create(user=user)
        login(request,user)
        return Response({'token'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#Coba Authentication
@swagger_auto_schema(
    method='get',
    tags=['Accounts'],
    responses={
        status.HTTP_200_OK: openapi.Response('User data', CustomUserSerializer),
        status.HTTP_401_UNAUTHORIZED: openapi.Response('Authentication failed', None)
    }
)
@api_view(['GET'])
def coba_authentication(request):
    if request.user.is_authenticated:
        print('Masuk Ngga')
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    print('Masuk')
    return Response('Authentication failed', status=status.HTTP_401_UNAUTHORIZED)