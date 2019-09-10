from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField, 
    PrimaryKeyRelatedField,
    CurrentUserDefault,
)
from rest_framework import serializers

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
        ]
        read_only_fields = (
            'id',
            'username',
        )


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()
