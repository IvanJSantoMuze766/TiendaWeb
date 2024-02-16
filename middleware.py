import logging
from django.shortcuts import render
from django.http import HttpResponseServerError

class CustomExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            response = self.handle_exception(request, e)

        return response

    def handle_exception(self, request, exception):
        # Registrar el error en el registro de errores
        logging.error(f"Error en la solicitud {request.path}: {exception}")

        # Renderizar una página de error personalizada
        return HttpResponseServerError(render(request, 'error_505.html'))
