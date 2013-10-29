#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import webob.exc
import operate_queue
from log.init_logger import DQ_LOGGER

logger = DQ_LOGGER


def index(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'current_date': now})


def show_message(request):
    now = datetime.datetime.now()
    return render_to_response('show_message.html', {'current_date': now})

def generate_queue_name(input_str):
    return 'q_' + input_str


def get_message(request):
    params = dict(request.REQUEST)
    if len(params) > 1:
        raise webob.exc.HTTPBadRequest('Too more parameters')

    user = params.get('user')
    if user == None:
        raise webob.exc.HTTPBadRequest('User name is None')

    queue_name = generate_queue_name(user)
    queues = operate_queue.get_queues()
    if queue_name not in queues:
        raise webob.exc.HTTPNotFound('Queue is not found')

    message = operate_queue.get_message_consume(queue_name)
    if message == None:
        message = ''
    return HttpResponse(str(message))


def put_message(request):
    params = dict(request.REQUEST)
    if len(params) > 4:
        raise webob.exc.HTTPBadRequest('Too more parameters')

    user = params.get('user').encode('utf8')
    message = params.get('message').encode('utf8')
    label = params.get('label').encode('utf8')
    delay = params.get('delay').encode('utf8')

    logger.debug('user %s, message %s, label %s, delay %s' % (user, message, label, delay))

    if user == None or message == None or label == None or delay == None:
        raise webob.exc.HTTPBadRequest('Parameters is invalid')

    queue_name = generate_queue_name(user)
    result = operate_queue.put_message(queue_name, message, delay=long(delay))
    if result:
        return HttpResponse()
    else:
        return HTTPServerError('Put message error')


def update_message(request):
    # TODO(tongkai): to do update message
    return HttpResponse()


def delete_message(request):
    # TODO(tongkai): to do delete message
    return HttpResponse()


def handle_message(request):
    if request.method == 'GET':
        return get_message(request)
    elif request.method == 'POST':
        return put_message(request)
    elif request.method == 'PUT':
        return update_message(request)
    elif request.method == 'DELETE':
        return delete_message(request)
    else:
        raise HTTPBadRequest('HTTP method is invalid')

