#!/usr/bin/python
# -*- coding: UTF-8 -*-

import beanstalkc

def connect(bean_host='localhost', bean_port=11300):
    return beanstalkc.Connection(bean_host, bean_port)


def put_message(queue_name, message, priority=1024, delay=0, ttr=120):
    beanstalk = connect()

    #tubes = beanstalk.tubes()
    beanstalk.use(queue_name)
    beanstalk.put(str(message), priority, delay, ttr)
    return True


def reput_message(queue_name, message, priority=1024, delay=60, ttr=120):
    put_message(queue_name, message, priority, delay, ttr)


def get_message(queue_name):
    beanstalk = connect()

    beanstalk.watch(queue_name)
    beanstalk.ignore('default')
    return beanstalk.reserve(timeout=0)


def get_message_view(queue_name):
    msg_obj = get_message(queue_name)
    message = None
    if msg_obj:
        message = msg_obj.body
    return message


def get_message_consume(queue_name):
    msg_obj = get_message(queue_name)
    message = None
    if msg_obj:
        message = msg_obj.body
        msg_obj.delete()
    return message


def get_queues():
    beanstalk = connect()
    return beanstalk.tubes()

