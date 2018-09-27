import os
import sys

sys.path.append(os.path.abspath('.\src'))
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
os.environ['PYTHONPATH'] = os.path.abspath('..') + ";" + os.path.abspath('.')

import logging
import threading
from random import randrange
from config.rabbitmq_conf import no_ack_status, rabbitmq_host

import pika

from config.custom_logging import LogConfig

logconf = LogConfig("rabbitmq_test", logging.DEBUG)
log = logconf.create_logger()

threads = []


def thread1_func(channel1):
    while True:
        num = randrange(0, 20)
        log.debug(f"Sending #{num}")
        channel1.basic_publish(exchange='', routing_key='input1', body=str(num))


def thread2_func(channel1, channel2):
    def receive1(ch, method, properties, body):
        num2 = int(body) * 2
        channel2.basic_publish(exchange='', routing_key='output1', body=str(num2))
        log.debug(f"Received #{body} sending to queue output1/server as {num2}")

    # a callback when message coming
    channel1.basic_consume(receive1, queue='input1', no_ack=no_ack_status)
    log.debug("channel1 start consuming..")
    channel1.start_consuming()


def thread3_func(channel3):
    def receive2(ch, method, properties, body):
        log.debug(f"Received final value #{body}")
        channel3.basic_ack(delivery_tag=method.delivery_tag)

    channel3.basic_consume(receive2, queue='output2', no_ack=no_ack_status)
    log.debug("channel3 start consuming..")
    channel3.start_consuming()


if __name__ == '__main__':
    connection1 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel1 = connection1.channel()
    channel1.queue_declare(queue='input1')

    connection2 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel2 = connection2.channel()
    channel2.queue_declare(queue='output1')

    connection3 = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel3 = connection3.channel()
    channel3.queue_declare(queue='output2')

    t1 = threading.Thread(target=thread1_func, args=(channel1,))
    t1.daemon = True
    threads.append(t1)

    t2 = threading.Thread(target=thread2_func, args=(channel1, channel2,))
    t2.daemon = True
    threads.append(t2)

    t3 = threading.Thread(target=thread3_func, args=(channel3,))
    t3.daemon = True
    threads.append(t3)

    t1.start()
    t2.start()
    t3.start()

    for t in threads:
        t.join()

    log.debug("Done..")
