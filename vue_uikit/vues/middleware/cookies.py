

class CookiesMiddleware(object):
    def process_request(self, request):
        return None

    def process_response(self, request, response):
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        return None
    pass