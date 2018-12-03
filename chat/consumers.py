# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from teamproject.models import *
from accounts.models import *
from django.utils import timezone

import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        teamId = text_data_json['teamId']
        sender = text_data_json['sender']
        message = text_data_json['chatMsg']
        sendedDate = timezone.now()

        team = Team.objects.get(pk=teamId)
        member = Member.objects.get(pk=sender)
        teamChat = TeamChat.objects.create(teamId = team, sender=member, chatMsg = message, sendedDate = sendedDate)
        teamChat.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': sender,
                'sendedDate': sendedDate.strftime("%Y-%m-%d %H:%M:%S"),
                'chatMsg': message,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        sender = event['sender']
        sendedDate = event['sendedDate']
        message = event['chatMsg']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'sender': sender,
            'sendedDate': sendedDate,
            'chatMsg': message,
        }))
