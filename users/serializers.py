from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField, 
    PrimaryKeyRelatedField,
)
from rest_framework import serializers

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone',
        ]
        read_only_fields = (
            'id',
            'email',
            'username',
        )


class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'phone',
        ]
        read_only_fields = (
            'id',
            'email',
        )


class UserDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk',
                  'date_joined',
                  'is_active',
                  'email',
                  'phone',
                  ]


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()
