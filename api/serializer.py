# api/serializer.py

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserProfile
from rest_framework.response import Response
from django.http import JsonResponse


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            token = super().get_token(user)
            # Add custom claims
            token['userName'] = user.userName
            token['password'] = user.password
            # ...
            return (token)
        except Exception as e:
            print('error', e)
            return JsonResponse(e, status=500)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('userName', 'firstName', 'lastName', 'organisation', 'email', 'password')

    def create(self, validated_data):

        try:
            if UserProfile.objects.filter(userName=validated_data['userName']).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            user = UserProfile.objects.create(
                userName=validated_data['userName'],
                password=validated_data['password'],
                firstName=validated_data['firstName'],
                lastName=validated_data['lastName'],
                organisation=validated_data['organisation'],
                email=validated_data['email'],
                active=True
            )

            user.set_password(validated_data['password'])
            user.save()

            print('done')
            return JsonResponse({'success': 'User created successfully'}, status=201)
        except Exception as e:
            print('error', e)
            return JsonResponse(e, status=500)

        