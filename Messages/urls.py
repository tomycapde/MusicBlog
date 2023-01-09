from django.urls import path
from .views import all_messages, new_message, chat, respond_message

urlpatterns = [
    path('all_messages/', all_messages, name='all_messages'),
    path('new_message/', new_message, name='new_message'),
    path('chat/<id>', chat, name='chat'),
    path('respond/<receiver>', respond_message, name='respond_message')
]