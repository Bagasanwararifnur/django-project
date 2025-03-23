from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
from datetime import timedelta
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
        # serializer.save()
        serializer_response = CustomUserSerializerGet(data=serializer.data)
        if serializer_response.is_valid():
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
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
        login(request,user)
        return Response('Login succesfully', status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#Coba Authentication
@swagger_auto_schema(
    method='get',
    tags=['Accounts'],
    responses={
        status.HTTP_200_OK: openapi.Response('Authorized',None),
        status.HTTP_401_UNAUTHORIZED: openapi.Response('Authentication failed', None)
    }
)
@api_view(['GET'])
def authorization_check(request):
    if request.user.is_authenticated:
        return Response('Authorized',status=status.HTTP_200_OK)
    return Response('Unauthorazied', status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(
    method='get',
    tags=['Accounts'],
    responses={
        status.HTTP_200_OK: openapi.Response('Logout', CustomUserSerializer),
        status.HTTP_401_UNAUTHORIZED: openapi.Response('Authentication failed', None)
    }
)
@api_view(['GET'])
def logout_account(request):
    print(request)
    if request.user.is_authenticated:
        print('Masuk')
        logout(request)
        return Response('Logout', status=status.HTTP_200_OK)
    return Response('Authentication failed', status=status.HTTP_401_UNAUTHORIZED)

#Email Test
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    operation_id='Email Send Test',
    manual_parameters=[
        openapi.Parameter('receiver_email', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def send_email_test(request):
    receiver_email = request.data.get('receiver_email')
    print(receiver_email)
    send_mail(
        'Test Email',
        f'This is a test email from Django API from {settings.EMAIL_HOST_USER}',
        f'{settings.EMAIL_HOST_USER}',
        [receiver_email],
        fail_silently=False,
    )
    return Response('Email sent successfully', status=status.HTTP_200_OK)

#Change Password
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    operation_id='Change Password',
    manual_parameters=[
        openapi.Parameter('old_password', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('new_password', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def change_password(request):
    if request.user.is_authenticated:
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()
            return Response('Password changed successfully', status=status.HTTP_200_OK)
        return Response('Old password is incorrect', status=status.HTTP_400_BAD_REQUEST)
    return Response('Authentication failed', status=status.HTTP_401_UNAUTHORIZED)

#Token Forgot Password
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    operation_id='Forgot Password',
    manual_parameters=[
        openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def forgot_password(request):
    email = request.data.get('email')
    user = CustomUser.objects.filter(email=email).first()
    if user:
        create_token = ForgotPassword(user=user)
        create_token.save()
        serializers = TokenPasswordSerializer(create_token)
        send_mail(
            'Password Reset (Test Django)',
            f'To reset your password, please visit this link: {serializers.data["token"]} (Test Django)',
            f'{settings.EMAIL_HOST_USER}',
            [email],
            fail_silently=False,
        )
        return Response('Email For Reset Password Has Been Send',status=status.HTTP_200_OK)
    return Response('User not found', status=status.HTTP_404_NOT_FOUND)

#Chang Password from Forgot Password Feature
@swagger_auto_schema(
    method='post',
    tags=['Accounts'],
    operation_id='Change Password from Forgot Password',
    manual_parameters=[
        openapi.Parameter('token', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('email',openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('new_password', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
    ]
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def change_password_forgot_password(request):
    token = request.data.get('token')
    email = request.data.get('email')
    new_password = request.data.get('new_password')

    try:
        token_uuid = uuid.UUID(token).hex
    except ValueError:
        return Response('Invalid token format', status=status.HTTP_400_BAD_REQUEST)

    try:
        check_token = ForgotPassword.objects.get(token=token, is_valid=True)
        if check_token.user.email == email:
            check_token.user.set_password(new_password)
            check_token.user.save()
            check_token.is_valid = False
            check_token.save()
            return Response('Password changed successfully', status=status.HTTP_200_OK)
    except ForgotPassword.DoesNotExist:
        return Response('Token not found or expired', status=status.HTTP_400_BAD_REQUEST)
    return Response('Invalid Process', status=status.HTTP_404_NOT_FOUND)
   


        


