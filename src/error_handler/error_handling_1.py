from flask import Flask, request
def my_function():
    if request.method == 'PUT':
        try:
            #a_test_function(request)
            return {
                'message': 'Request is a good request.',
                'status': 200,
            }, 200
        except ValueError as error:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(error),
            }, 400
        except:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': 'Unexpected error.',
            }, 400
