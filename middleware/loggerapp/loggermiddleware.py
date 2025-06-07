from .models import Requestlog
import traceback

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    

    def __call__(self, request):
        try:
            response = self.get_response(request)
            status_code = response.status_code
            error = None
        except Exception as e:
            status_code = 500
            error = traceback.format_exc()
            response = self.get_response(request)


        Requestlog.objects.create(
            path=request.path,
            method = request.method,
            status_code = status_code,
            error_message = error
        )

        return response
