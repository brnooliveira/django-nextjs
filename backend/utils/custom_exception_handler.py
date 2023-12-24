from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if exception_class == 'AuthenticationFailed':
        response.data = {
            'error': 'Invalid Password or Email. Please try again!'
        }
    if exception_class == 'NotAuthenticated':
        response.data = {
            'error': 'Login first to access this resource!'
        }

    if exception_class == 'InvalidToken':
        response.data = {
            'error': 'Invalid Token!'
        }
    return response
