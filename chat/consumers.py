import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Chat, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
        await self.close()

    def create_message(self, text):
        message = Message.objects.create(text=text)
        return message



    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        message = await database_sync_to_async(self.create_message)(text=data['text'])
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat.message', 'data': data}
        )

    async def chat_message(self, event):
        data = event['data']

        await self.send(json.dumps(data))
