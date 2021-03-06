from django.db import models
from django.conf import settings


class Meetup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meetup_organizer')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    date = models.DateField(null=True)
    time = models.CharField(max_length=120, null=True)
    venue = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Question(models.Model):
    meetup = models.ForeignKey(Meetup, on_delete=models.CASCADE, related_name='meetup_question')
    text = models.CharField(max_length=250, default="")
    upvotes = models.SmallIntegerField(default=0)
    downvotes = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.meetup)

