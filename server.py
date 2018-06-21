from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

# add function
@dispatcher.add_method
def calculation(**kwargs):
    x_value = kwargs["x"]
    y_value = 3.8*x_value*(1-x_value)
    return y_value


@Request.application
def application(request):

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4000, application)
