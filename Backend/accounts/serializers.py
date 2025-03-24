from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'bio']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CustomUserSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'bio']

class TokenPasswordSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = ForgotPassword
        fields = ['token','email']

    def get_email(self, obj):
        return obj.user.email
    def get_token(self, obj):
        return obj.token.hex



    

