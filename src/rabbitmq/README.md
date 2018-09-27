#### Notes

Still got error below, seems that pika lib is unreliable.

Exception in thread Thread-2:
Traceback (most recent call last):
  File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "server.py", line 41, in thread2_func
    channel2.start_consuming()
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 1822, in start_consuming
    self.connection.process_data_events(time_limit=None)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 749, in process_data_events
    self._flush_output(common_terminator)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 477, in _flush_output
    result.reason_text)
pika.exceptions.ConnectionClosed: (505, 'UNEXPECTED_FRAME - expected content header for class 60, got non content header frame instead')

Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "server.py", line 30, in thread1_func
    channel1.start_consuming()
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 1822, in start_consuming
    self.connection.process_data_events(time_limit=None)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 758, in process_data_events
    self._dispatch_channel_events()
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 521, in _dispatch_channel_events
    impl_channel._get_cookie()._dispatch_events()
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 1445, in _dispatch_events
    evt.body)
  File "server.py", line 24, in receive1_func
    channel2.basic_publish(exchange='', routing_key='internal', body=body)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 2120, in basic_publish
    mandatory, immediate)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/adapters/blocking_connection.py", line 2206, in publish
    immediate=immediate)
  File "/home/bondhan/workspace/python/PyBono/env/lib/python3.6/site-packages/pika/channel.py", line 415, in basic_publish
    raise exceptions.ChannelClosed()
pika.exceptions.ChannelClosed
