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
  timestamp = models.TimeField(auto_now=True)
  title = models.CharField(max_length=200)
  body = models.CharField(max_length=5000)
  sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE, db_constraint=False)
  receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, db_constraint=False)
  read = models.BooleanField(default=False)
  senderDel = models.BooleanField(default=False)
  receiverDel = models.BooleanField(default=False)