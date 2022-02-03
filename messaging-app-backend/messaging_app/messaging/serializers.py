from rest_framework import serializers
from .models import User, Message, Outbox, Inbox

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email')
  
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('id', 'timestamp', 'title', 'body', 'receiver_id', 'sender_id')

class OutboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Outbox
    fields = ('id', 'deleted', 'message_id', 'user_id')

class InboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Inbox
    fields = ('id', 'deleted', 'read', 'message_id', 'user_id')