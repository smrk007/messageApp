from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User as DjUser

from .models import User, Message
from .serializers import *

@api_view(['POST'])
def user_list(request):

  if request.method == 'POST':
    serializer =  UserSerializer(data=request.data)
    if serializer.is_valid():
      print(serializer.validated_data['username'])
      user = DjUser.objects.create(
        username=serializer.validated_data['username'],
        email=serializer.validated_data['email']
      )
      user.set_password(serializer.validated_data['password'])
      user.save()
      serializer.save()
      return Response(status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_details(request, id):

  try:
    user = User.objects.get(id=id)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'PUT':
    serializer = UserSerializer(user, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def message_list(request):

  if request.method == 'POST':
    # User must include a recipient
    if 'recipient' not in request.data:
      return Response('Missing recipient.', status=status.HTTP_400_BAD_REQUEST)
    try:
      recipient = DjUser.objects.get(username=request.data['recipient'])
    except:
      return Response('Recipient does not exist.', status=status.HTTP_400_BAD_REQUEST)

    request.data['receiver_id'] = recipient.id
    request.data['sender_id'] = request.user.id

    messageSerializer =  MessageSerializer(data=request.data)
    if messageSerializer.is_valid():
      messageSerializer.save()
      print(messageSerializer)
      return Response(status=status.HTTP_201_CREATED) 
    return Response(messageSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def message_details(request, id):

  try:
    message = Message.objects.get(id=id)
  except Message.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'PUT':
    serializer = MessageSerializer(message, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    message.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def inbox_list(request):

  if request.method == 'GET':
    data = Inbox.objects.all()
    serializer = InboxSerializer(data, context={'request', request}, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer =  InboxSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def inbox_details(request, id):

  try:
    inbox = Inbox.objects.get(id=id)
  except Inbox.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'PUT':
    serializer = InboxSerializer(inbox, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    inbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def outbox_list(request):

  if request.method == 'GET':
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