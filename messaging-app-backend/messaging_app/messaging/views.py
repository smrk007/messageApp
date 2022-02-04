from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User as DjUser

from .models import Message
from .serializers import *

@api_view(['POST'])
def user_list(request):
  serializer =  UserSerializer(data=request.data)
  if serializer.is_valid():
    print(serializer.validated_data['username'])
    user = DjUser.objects.create(
      username=serializer.validated_data['username'],
      email=serializer.validated_data['email']
    )
    print('password', serializer.validated_data['password'])
    user.set_password(serializer.validated_data['password'])
    user.save()
    serializer.save()
    return Response(status=status.HTTP_201_CREATED) 
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def message_list(request):
  # User must include a recipient
  if 'recipient' not in request.data:
    return Response('Missing recipient.', status=status.HTTP_400_BAD_REQUEST)
  try:
    recipient = DjUser.objects.get(username=request.data['recipient'])
  except:
    return Response({'username': ['Recipient does not exist.']}, status=status.HTTP_400_BAD_REQUEST)

  request.data['receiver_id'] = recipient.id
  request.data['sender_id'] = request.user.id

  messageSerializer =  MessageSerializer(data=request.data)
  if messageSerializer.is_valid():
    messageSerializer.save()
    print(messageSerializer)
    return Response(status=status.HTTP_201_CREATED) 
  return Response(messageSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inbox_list(request):
  data = Message.objects.filter(receiver_id=request.user.id, receiverDel=False)
  serializer = MessageSerializer(data, context={'request', request}, many=True)
  for item in serializer.data:
    item['recipient'] = DjUser.objects.get(id=item['receiver_id']).username
    item['sender'] = DjUser.objects.get(id=item['sender_id']).username
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def inbox_details(request, id):
  try:
    message = Message.objects.get(id=id)
    message.receiverDel = True
    message.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except Message.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def outbox_list(request):
  data = Message.objects.filter(sender_id=request.user.id, senderDel=False)
  serializer = MessageSerializer(data, context={'request', request}, many=True)
  for item in serializer.data:
    item['recipient'] = DjUser.objects.get(id=item['receiver_id']).username
    item['sender'] = DjUser.objects.get(id=item['sender_id']).username
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def outbox_details(request, id):
  try:
    message = Message.objects.get(id=id)
    message.senderDel = True
    message.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except Message.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)