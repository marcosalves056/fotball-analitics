from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

class DetectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Conectado ao WebSocket!"}))

    async def disconnect(self, close_code):
        print("Desconectado")

    async def receive(self, text_data):
        data = json.loads(text_data)
        video = data.get("video", "sem_nome.mp4")

        for i in range(3):
            await self.send(text_data=json.dumps({"progress": f"Processando frame {i} de {video}"}))
            await asyncio.sleep(1)

        await self.send(text_data=json.dumps({"result": f"✅ Finalizado: {video}"}))
