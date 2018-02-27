from django.utils.deprecation import MiddlewareMixin
from ..tools.utils import data_decrypt, data_encrypt
import json

CSRF_TOKEN_CHECK = 'CSRF_TOKEN_CHECK'


class CookiesMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # try:
        #     cookie = request.COOKIES[CSRF_TOKEN_CHECK]
        #     username = request.COOKIES['username']
        #     if request.META.get('HTTP_X_FORWARDED_FOR'):
        #         ip = request.META['HTTP_X_FORWARDED_FOR']
        #     else:
        #         ip = request.META['REMOTE_ADDR']
        #
        #     if data_decrypt(concat_cookies(ip, username), cookie):
        #         print('check success')
        #     else:
        #         print('check error')
        # except KeyError:
        #     pass
        # if data_decrypt()
        # print(request.COOKIES)
        return None


    def process_response(self, request, response):

        # if request.method == 'GET':
        #     # \
        #     #     or request.path != '/vues/register/' \
        #     #     or request.path != '/vues/login/':
        #     return response
        #
        # data = json.loads(response.content)
        # # print(json.loads(data))
        #
        # if data['errorCode'] == 0:
        #
        #     if request.META.get('HTTP_X_FORWARDED_FOR'):
        #         ip = request.META['HTTP_X_FORWARDED_FOR']
        #     else:
        #         ip = request.META['REMOTE_ADDR']
        #
        #     print(ip)
        #     if request.POST['username']:
        #         response.set_cookie(CSRF_TOKEN_CHECK, data_encrypt(concat_cookies(ip, request.POST['username'])))
        #         response.set_cookie('username', request.POST['username'])
        #     return response
        # else:
            return response

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    #     return None


def concat_cookies(ip, username):
    return ip + ':+:' + username