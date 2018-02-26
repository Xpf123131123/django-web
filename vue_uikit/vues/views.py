from django.shortcuts import render, render_to_response
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from .models import User
from .tools import errorCode
import json


# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'vues/index.html'


class HomeView(generic.DetailView):
    template_name = ''

    def get_queryset(self):
        pass


class RegisterView(generic.FormView):
    template_name = 'vues/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'vues/register.html', {
            'app_path': '/vues/register/',
            'next': '../'
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
            resp = {'errorCode': errorCode.userHasBeenExits,
                    'errormsg': '用户已存在',
                    'message': {}
                    }
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            if user:
                resp = {'errorCode': 0,
                        'errormsg': '',
                        'message': {
                            'next': '../'
                        }}
            else:
                resp = {'errorCode': errorCode.serverBusy,
                        'errormsg': '服务器繁忙',
                        'message': {
                            'next': '../'
                        }}
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


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

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                resp = {'errorCode': 0,
                        'errormsg': '',
                        'message': {
                            'next': '../'
                        }}
            else:
                # Return a 'disabled account' error message
                resp = {'errorCode': errorCode.userOrPasswordError,
                        'errormsg': '用户名或密码错误',
                        'message': {}
                        }
        else:
            # Return an 'invalid login' error message.
            resp = {'errorCode': errorCode.userDoesNotExits,
                    'errormsg': '用户不存在',
                    'message': {}
                    }
        # if request.META.get('HTTP_X_FORWARDED_FOR'):
        #     ip = request.META['HTTP_X_FORWARDED_FOR']
        # else:
        #     ip = request.META['REMOTE_ADDR']

        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


def getResp(message, errorCode, errormsg):
    resp = {
        'errorCode': errorCode,
        'errormsg': errormsg,
        'message': message
    }
    return resp