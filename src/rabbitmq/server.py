import os
import sys

sys.path.append(os.path.abspath('.\src'))
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
os.environ['PYTHONPATH'] = os.path.abspath('..') + ";" + os.path.abspath('.')

import logging
import threading
import pika

from config.custom_logging import LogConfig
from config.rabbitmq_conf import no_ack_status, rabbitmq_host

logconf = LogConfig("rabbitmq_test", logging.DEBUG)
log = logconf.create_logger()

threads = []


def thread1_func(channel1, channel2):
    def receive1_func(ch, method, properties, body):
        channel2.basic_publish(exchange='', routing_key='internal', body=body)
        log.debug(f"Receive #{body} and send directly #{body} to queue internal")
        channel1.basic_ack(delivery_tag=method.delivery_tag)

    channel1.basic_consume(receive1_func, queue='output1', no_ack=no_ack_status)
    log.debug("channel1 start consuming..")
    channel1.start_consuming()


def thread2_func(channel2, channel3):
    def receive2_func(ch, method, properties, body):
        num = int(body) * 3
        log.debug(f"Receive #{body}, multiply by 3 and send directly #{num} to queue output2")
        channel3.basic_publish(exchange='', routing_key='output2', body=str(num))

    channel2.basic_consume(receive2_func, queue='internal', no_ack=no_ack_status)
    log.debug("channel2 start consuming..")
    channel2.start_consuming()


if __name__ == '__main__':
    connection1 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel1 = connection1.channel()
    channel1.queue_declare(queue='output1')

    connection2 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel2 = connection2.channel()
    channel2.queue_declare(queue='internal')

    connection3 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel3 = connection3.channel()
    channel3.queue_declare(queue='output2')

    t1 = threading.Thread(target=thread1_func, args=(channel1, channel2,))
    t1.daemon = True
    threads.append(t1)

    t2 = threading.Thread(target=thread2_func, args=(channel2, channel3,))
    t2.daemon = True
    threads.append(t2)

    t1.start()
    t2.start()

    for t in threads:
        t.join()
