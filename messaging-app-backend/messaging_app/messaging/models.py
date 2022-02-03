from django.db import models
from django.contrib.auth.models import User

# CONSTANTS
USERNAME_LENGTH = 128
ID_LENGTH = 36

class User(models.Model):
  username = models.CharField(max_length=USERNAME_LENGTH, unique=True)
  password = models.CharField(max_length=128)
  email = models.EmailField(max_length=128)

class Message(models.Model):
  timestamp = models.TimeField()
  title = models.CharField(max_length=200)
  body = models.CharField(max_length=5000)
  sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
  receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

class Outbox(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.ForeignKey(Message, on_delete=models.CASCADE)
  deleted = models.BooleanField()

class Inbox(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.ForeignKey(Message, on_delete=models.CASCADE)
  deleted = models.BooleanField()
  read = models.BooleanField()