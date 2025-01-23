from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # Extend later if needed

class ChatRoom(models.Model):
    participants = models.ManyToManyField(User)

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
