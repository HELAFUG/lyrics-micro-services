from faststream import FastStream
from faststream.kafka import KafkaBroker
from core.config import settings

fs_broker = KafkaBroker(bootstrap_servers=settings.kafka.url)

fs_app = FastStream(broker=fs_broker)
