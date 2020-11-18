from aiokafka import AIOKafkaConsumer
from settings import kafka_settings


async def before_server_start(app, loop):
    app.kafka_consumer = AIOKafkaConsumer('user_auth_topic', loop=loop,
                                          bootstrap_servers='{host}:{port}'.format(**kafka_settings))
    await app.kafka_consumer.start()


async def after_server_stop(app, loop):
    await app.kafka_consumer.stop()


listeners = (
    before_server_start,
    after_server_stop,
)
