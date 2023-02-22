from django.contrib.auth.hashers import make_password, check_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

    def create(self, validated_data):
        email = Email()
        email.email = validated_data['email']
        email.user = validated_data['user']

        email.save()
        return email



class UserSerializer(serializers.ModelSerializer):

    email = EmailSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        user = User()
        user.name = validated_data['name']
        user.last_name = validated_data['last_name']
        user.address = validated_data['address']
        user.birthday = validated_data['birthday']
        user.about = validated_data['about']
        user.save()

        return user

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
