"""messaging_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from messaging import views

urlpatterns = [
  path('auth/', obtain_auth_token, name="auth"),
  re_path(r'^api/user/$', views.user_list),
  re_path(r'^api/user/([0-9]+)$', views.user_details),
  re_path(r'^api/message/$', views.message_list),
  re_path(r'^api/message/([0-9]+)$', views.message_details),
  re_path(r'^api/inbox/$', views.inbox_list),
  re_path(r'^api/inbox/([0-9]+)$', views.inbox_details),
  re_path(r'^api/outbox/$', views.outbox_list),
  re_path(r'^api/outbox/([0-9]+)$', views.outbox_details)
]
