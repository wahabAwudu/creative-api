from rest_framework.serializers import ModelSerializer
from .models import Key


class KeySerializer(ModelSerializer):
    class Meta:
        model = Key
        fields = [
            'id', 'text', 'used', 'created_at','updated_at'
        ]
        read_only_fields = (
            'id', 'text', 'created_at', 'updated_at',
        )
