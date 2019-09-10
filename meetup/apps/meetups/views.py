# drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)
from rest_framework.decorators import api_view, list_route
from rest_framework.views import APIView
from allauth.account.views import ConfirmEmailView

# django imports
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# apps imports
from .serializers import (
    MeetupModelSerializer,
    QuestionModelSerializer
)

from .models import Meetup, Question

class MeetupModelViewSet(ModelViewSet):
    model = Meetup
    permission_classes = [IsAuthenticated]
    serializer_class = MeetupModelSerializer

    def get_queryset(self):
        return Meetup.objects.filter(user=self.request.user.id)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(serializer.data))


class QuestionModelViewSet(ModelViewSet):
    model = Question
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionModelSerializer

    def get_queryset(self):
        return Question.objects.filter(meetup=self.request['id'])
    
    def create(self, request, *args, **kwargs):
        meetup = Meetup.objects.get(id=request.data['meetup_id'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(meetup=meetup, text=request.data['text'])
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(serializer.data))
    
    @list_route(methods=['POST'])
    def add_upvotes(self, request):
        question = Question.objects.get(id=request.data['question_id'])
        question.upvotes = question.upvotes + 1
        question.save()
        serializer = self.get_serializer(question)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @list_route(methods=['POST'])
    def add_downvotes(self, request):
        question = Question.objects.get(id=request.data['question_id'])
        question.downvotes = question.downvotes - 1
        question.save()
        serializer = self.get_serializer(question)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
