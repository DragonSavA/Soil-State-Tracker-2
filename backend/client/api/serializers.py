from rest_framework import serializers
from rest_framework.authtoken.models import Token

from client.models import Client

class TokenSerialzizer(serializers.Serializer):
    '''Сериализация ключа токена'''
    
    token = serializers.CharField()

class ClientActivitySerializer(serializers.ModelSerializer):
    '''Сериализация активности контакта'''

    class Meta:
        model = Client
        fields = ['is_active']

class ClientMeSerialzier(serializers.ModelSerializer):
    '''Для сериализации пользователя'''

    class Meta:
        model = Client
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff']