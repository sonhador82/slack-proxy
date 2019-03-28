# -*- coding: utf-8 -*-

from time import sleep
import os
import requests
from celery import Celery

REDIS_HOST = os.environ.get('REDIS_HOST', default=None)
if not REDIS_HOST:
    raise ValueError("No broker host")

broker_conn = 'redis://{}/0'.format(REDIS_HOST)
app = Celery('tasks', backend=broker_conn, broker=broker_conn)
webhook_url = 'https://hooks.slack.com/services/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'
channel = '@d.shelestovskiy'


def _get_color_from_level(level):
    color = ''
    if level == 'WARNING':
        color = ':alert-warn:'
    elif level == 'CRITICAL':
        color = ':alert-critical:'
    elif level == 'OK':
        color = ':alert-ok:'
    return color


@app.task
def send(event):
    global webhook_url, channel
    data = {
        'channel': channel,
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '{} {}'.format(
                        _get_color_from_level(event['level']),
                        event['message']
                    )
                }
            }
        ]
    }
    for i in range(2, 20, 2):
        r = requests.post(webhook_url, json=data)
        if r.status_code == 200:
            break
        sleep(i)
    return r.reason
