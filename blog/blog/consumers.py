import json
from channels.generic.websocket import AsyncWebsocketConsumer

'''
django连接channels的视图类
'''
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        # 加入聊天组,并监听对应的频道
        # self.channel_layer进行监听频道
        # self.scope['user'].username以用户名作为组名，
        # self.channel_name 要进行监听的频道，会自己生成唯一的频

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
                {
                    'type': 'chat_message',
                    'message':self.scope['user'].username+": "  +message
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            {"message":message}
        ))
