from rest_framework import serializers
from .models import User, Message

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email')
  
class MessageSerializer(serializers.ModelSerializer):
  receiver_id = serializers.IntegerField()
  sender_id = serializers.IntegerField()

  class Meta:
    model = Message
    fields = ('id', 'title', 'body', 'receiver_id', 'sender_id')