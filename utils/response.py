from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class Result():

    def __init__(self, status, message, data, next_page=False):
        self.status = status
        self.message = message
        self.data = data
        self.next = next_page

    def json(self):
        status = 'success'
        if self.status is False:
            status = 'error'
        return {
            'status': status,
            'message': self.message,
            'data': self.data
        }

    @classmethod
    def success(cls, data, message=''):
        result = cls(True, message, data)
        return Response(data=result.json(), status=status.HTTP_200_OK)

    @classmethod
    def created(cls, data, message=''):
        result = cls(True, message, data)
        return Response(data=result.json(), status=status.HTTP_201_CREATED)

    @classmethod
    def bad_request(cls, data, message=''):
        result = cls(False, message, data)
        return Response(data=result.json(), status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def forbidden(cls, data, message=''):
        result = cls(False, message, data)
        return Response(data=result.json(), status=status.HTTP_403_FORBIDDEN)

    @classmethod
    def not_found(cls, data, message='not found'):
        result = cls(False, message, data)
        return Response(data=result.json(), status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def server_error(cls, data, message='internal server error'):
        result = cls(False, message, data)
        return Response(data=result.json(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Update the structure of the response data.
    if response is not None:
        customized_response = {}
        customized_response['status'] = "error"
        try:
            for key, value in response.data.items():
                if isinstance(value, list):
                    if key == "non_field_errors":
                        error = value[0]
                    else:
                        error = key + " " + value[0]
                    customized_response['message'] = error
                else:
                    error = value
                    customized_response['message'] = error
            response.data = customized_response
            customized_response['data'] = {}

        except:
            for value in response.data:
                error = key +" " + value
                print(response.data)
                customized_response['message'] = error

            response.data = customized_response
            customized_response['data'] = {}
    return response
