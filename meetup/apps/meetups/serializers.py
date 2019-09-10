from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField, 
    PrimaryKeyRelatedField,
    CurrentUserDefault,
)
from rest_framework import serializers

from .models import Meetup, Question


class MeetupModelSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(default=CurrentUserDefault(), read_only=True)
    questions = SerializerMethodField()

    class Meta:
        model = Meetup
        fields = [
            'id',
            'user',
            'title',
            'description',
            'questions',
            'created_at',
            'updated_at',
        ]
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

    def get_questions(self, obj):
        question = Question.objects.filter(meetup=obj)
        return QuestionModelSerializer(question, many=True).data


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'meetup',
            'text',
            'upvotes',
            'downvotes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = (
            'id',
            'meetup',
            'upvotes',
            'downvotes',
            'created_at',
            'updated_at',
        )
