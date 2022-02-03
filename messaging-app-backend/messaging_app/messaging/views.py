from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Message, Outbox, Inbox
from .serializers import *

@api_view(['GET', 'POST'])
def user_list(request):

  if request.method == 'GET':
    data = User.objects.all()
    serializer = UserSerializer(data, context={'request', request}, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer =  UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
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

@api_view(['GET', 'POST'])
def message_list(request):

  if request.method == 'GET':
    data = Message.objects.all()
    serializer = MessageSerializer(data, context={'request', request}, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer =  MessageSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
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

@api_view(['GET', 'POST'])
def outbox_list(request):

  if request.method == 'GET':
    data = Outbox.objects.all()
    serializer = OutboxSerializer(data, context={'request', request}, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer =  OutboxSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def outbox_details(request, id):
  try:
    outbox = Outbox.objects.get(id=id)
  except Outbox.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'PUT':
    serializer = OutboxSerializer(outbox, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    outbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)