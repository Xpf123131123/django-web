from django.shortcuts import render, reverse
from django.http import Http404, HttpResponse
from django.views import generic
from .models import User
from .tools.utils import decrypt

private_key = 'MIICWwIBAAKBgQCnIEESanWuyWqK36D546V7fbj3mVSh+ZeSPtrP+FlGYZ5NBrTHHickNquXbFsm3EePprgd+rCliH+ppjFEjFR/bMbXoFABno/p1EY1hiXJIBsnIfjadw47Mr2S1QgsKugnRgKkGGHbP0Byz+BEI8o7OEGJfYiktbhQ384nFzuFjQIDAQABAoGAX2Y3/u0qVCXBXZid6UcbVUzE4wFxoCw7a03Z1dFsFJLwrANh+i+qJC/Y70z5E0u2xbdjbimF4Ff0l8C4auq36ECAzT7ckSoy2uR9EQfGQIPKwu3MnrmhLw9Tv99poV41vB8NYdrhlrVJQ2Ajvz92j/cmO9Sf98Gov2SZ4sFtAPkCQQDbTwtj71LFqqfQfkrdebga38bVnTEa5kh9wX7iLjcIdl6ql4vEvdcJIxMBNLwSB447WaNl2MwfuO/QAQHpnInLAkEAwxY7EZ+SIN77bQqnW7E5ZPVBxjWOPvbL2TFZmnSsqtVZKzjxUb37YLhTHFFYAkhdwrX6hSZ9KjAmRTWyx7cjBwJAe7iACIS/AVxhB7H3sjI0tpR/q4reZPp88tTyK88+pLuCdGLCKt+eLD1pP0jswI8aokjTcWV44nyGbaXj2lLBOQJAd9Qs3itUt8ofR6AWolSee2vGRfhZckVnevY8IopuENTRW6IzYFFAme0+Z5NzapuGs/XRdn3ovcQrjbFpKhFMewJAD/M/fddedwFiQ0B09uWg9WSWNsyTP5EC+NZp8EzKZb2X7jquWJHDYRyr9LTyc4PPLTkyxPtcKfG2h5tEHxbbMw=='

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'


class LoginView(generic.FormView):
    template_name = 'polls/login.html'


def index(request):
    return HttpResponse("Hello django")


def login(request):

    if request.method == 'GET':
        # print('---------------')

        with open('polls/tools/master-public.pem') as f:
            key = f.read()
        return render(request, 'polls/login.html', {
            'app_path': '../../polls/login/',
            'public_key': key
        })

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password') # 加密
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=username)

            if user.password == password:
                print('*************************')
                print('user login success:\n{}'.format(user))
                print('*************************')
            else:
                print('*************************')
                print('warning: password error:\n{}'.format(user))
                print('*************************')
        except User.DoesNotExist:
            p = User.objects.create(username=username, password=password, email=email)
            print('*************************')
            print('user sign in success:\n{}'.format(p))
            print('*************************')

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        print('ip:', ip)
        response = render(request, 'polls/index.html')

        if request.POST['username']:
            response.set_cookie('username', request.POST['username'])
        return response

    return Http404
