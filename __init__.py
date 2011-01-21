
class IgnoreCsrfMiddleware(object):
    def process_request(self, request):
        request.csrf_processing_done = True
