from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import ContactList,MessageContactList,AddContact
app_name='message'

urlpatterns = [

    path('',ContactList.as_view(),name='contact-list'),
    path('<pk>/',MessageContactList.as_view(),name='send-message'),
    path('add/',AddContact.as_view(),name='add-contact')
]