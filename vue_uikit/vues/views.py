from django.shortcuts import render, render_to_response
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from .models import User
import json


# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'vues/index.html'


# @require_http_methods(["GET", "POST"])
# @never_cache
class RegisterView(generic.FormView):
    template_name = 'vues/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'vues/register.html', {
            'app_path': '/vues/register/'
        })

    def post(self, request, *args, **kwargs):
        print('**********************')
        print(request.POST)
        print('**********************')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            User.objects.get(username=username)
            resp = {'errorCode': 1002,
                    'errormsg': '用户已存在',
                    'message': {}
                    }
        except User.DoesNotExist:
            user = User.objects.create(username=username, email=email, password=password)
            if user:
                resp = {'errorCode': 0,
                        'errormsg': '',
                        'message': {
                            'next': '../'
                        }}
            else:
                resp = {'errorCode': 1004,
                        'errormsg': '服务器繁忙',
                        'message': {
                            'next': '../'
                        }}
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


# @require_http_methods(["GET", "POST"])
# @never_cache
class LoginView(generic.FormView):
    template_name = 'vues/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'vues/login.html', {
            'app_path': '/vues/login/'
        })

    def post(self, request, *args, **kwargs):
        print('**********************')
        print(request.POST)
        print('**********************')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            resp = getResp(user.password, password)[0]
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
                resp = getResp(user.password, password)[0]
            except User.DoesNotExist:
                resp = {'errorCode': 1001,
                        'errormsg': '用户不存在',
                        'message': {}
                        }

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


def getResp(password_sql, password_req):
    if password_sql == password_req:
        print('*************************')
        print('user login success')
        print('*************************')
        resp = {'errorCode': 0,
                'errormsg': '',
                'message': {
                    'next': '../'
                }}
        return resp, True
    else:
        print('*************************')
        print('warning: password error')
        print('*************************')

        resp = {'errorCode': 1003,
                'errormsg': '用户名或密码错误',
                'message': {}
                }
        return resp, False
