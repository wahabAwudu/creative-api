from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Key
from .serializers import KeySerializer

from .utils import generate_key

class KeyViewSet(ModelViewSet):
    model = Key
    serializer_class = KeySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Key.objects.all().order_by('-updated_at')

    def create(self, request, *args, **kwargs):
        new_key = generate_key()
        key = Key.objects.filter(text=new_key)

        while key.exists():
            new_key = generate_key()
            key = Key.objects.filter(text=new_key)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(text=new_key)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
