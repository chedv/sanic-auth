from settings import kafka_settings
import asyncio


async def fetch_kafka_message(app):
    await asyncio.sleep(kafka_settings['fetch'])

    async for message in app.kafka_consumer:
        print(message.topic, message.value.decode())


tasks = (
    fetch_kafka_message,
)
