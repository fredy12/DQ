# Create your views here.
from django.http import HttpResponse
import webob.exc
import operate_queue


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
    if len(params) > 3:
        raise webob.exc.HTTPBadRequest('Too more parameters')

    user = params.get('user')
    message = params.get('message')
    label = params.get('label')

    if user == None or message == None or label == None:
        raise webob.exc.HTTPBadRequest('Parameters is invalid')

    queue_name = generate_queue_name(user)
    result = operate_queue.put_message(queue_name, message)
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

