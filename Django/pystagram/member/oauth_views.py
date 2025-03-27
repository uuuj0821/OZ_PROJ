from urllib.parse import urlencode, parse_qs

import requests
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.core import signing
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import RedirectView

from member.forms import NicknameForm

User = get_user_model()

NAVER_CALLBACK_URL = '/oauth/naver/callback/'
NAVER_STATE = 'naver_login'
NAVER_LOGIN_URL = 'https://nid.naver.com/oauth2.0/authorize' # 요청url
NAVER_TOKEN_URL = 'https://nid.naver.com/oauth2.0/token'
NAVER_PROFILE_URL = 'https://openapi.naver.com/v1/nid/me'

GITHUB_CALLBACK_URL = '/oauth/github/callback/'
GITHUB_STATE = 'github_login'
GITHUB_LOGIN_URL = 'https://github.com/login/oauth/authorize' # 요청url
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_PROFILE_URL = 'https://api.github.com/user'

class NaverLoginRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        domain = self.request.scheme + '://' + self.request.META.get('HTTP_HOST', '') # https://locatlhost:8000 or https://127.0.0.1:8000
        callback_url = domain + NAVER_CALLBACK_URL

        print('callback_url : ', callback_url)

        state = signing.dumps(NAVER_STATE) # 암호화

        params = {
            'response_type': 'code',
            'client_id': settings.NAVER_CLIENT_ID,
            'redirect_uri': callback_url,
            'state': state
        }

        return f'{NAVER_LOGIN_URL}?{urlencode(params)}'

def naver_callback(request):
    print("=== 콜백 함수 진입 ===")
    code = request.GET.get('code')
    state = request.GET.get('state')

    # state 복호화(signing.loads)해서 확인
    if NAVER_STATE != signing.loads(state):
        raise Http404

    access_token = get_naver_access_token(code, state)

    # def get_access_token으로 선언
    # params = {
    #     'grant_type': 'authorization_code', # 발급
    #     'client_id': settings.NAVER_CLIENT_ID,
    #     'client_secret': settings.NAVER_SECRET,
    #     'code': code,
    #     'state': state
    # }
    #
    # response = requests.get(NAVER_TOKEN_URL, params=params)
    # result = response.json()
    # def get_access_token으로 선언_end

    profile_response = get_naver_profile(access_token)

    # 여러 함수에서 호출하므로 따로 함수로 만들어줌
    # # 회원정보 요청 (oauth로 받은 token과 같이 재요청)
    # headers = {
    #     'Authorization': f'Bearer {access_token}'
    # }
    #
    # # 회원정보 응답
    # response = requests.get(NAVER_PROFILE_URL, headers=headers)
    #
    # if response.status_code != 200:
    #     raise Http404
    #
    # result = response.json()
    # 여러 함수에서 호출하므로 따로 함수로 만들어줌_end

    print('profile request', profile_response)

    email = profile_response.get('email')
    print('email', email)

    user = User.objects.filter(email=email).first()
    print('user', user)

    if user:
        if not user.is_active:
            user.is_active = True
            user.save()

        login(request, user)
        return redirect('main')
    return redirect(reverse('oauth:nickname') + f'?access_token={access_token}&oauth=naver')


class GithubLoginRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        domain = self.request.scheme + '://' + self.request.META.get('HTTP_HOST', '') # https://locatlhost:8000 or https://127.0.0.1:8000
        callback_url = domain + GITHUB_CALLBACK_URL

        print('callback_url : ', callback_url)

        state = signing.dumps(GITHUB_STATE) # 암호화

        params = {
            'response_type': 'code',
            'client_id': settings.GITHUB_CLIENT_ID,
            'redirect_uri': callback_url,
            'state': state
        }

        return f'{GITHUB_LOGIN_URL}?{urlencode(params)}'

def github_callback(request):
    print("=== 콜백 함수 진입 ===")
    code = request.GET.get('code')
    state = request.GET.get('state')

    # state 복호화(signing.loads)해서 확인
    if GITHUB_STATE != signing.loads(state):
        raise Http404

    access_token = get_github_access_token(code, state)

    if not access_token:
        raise Http404

    profile_response = get_github_profile(access_token)
    print('profile request', profile_response)

    email = profile_response.get('email')
    print('email', email)

    user = User.objects.filter(email=email).first()
    print('user', user)

    if user:
        if not user.is_active:
            user.is_active = True
            user.save()

        login(request, user)
        return redirect('main')
    return redirect(reverse('oauth:nickname') + f'?access_token={access_token}&oauth=github')


def oauth_nickname(request):
    access_token = request.GET.get('access_token')
    oauth = request.GET.get('oauth')

    if not access_token or oauth not in ['naver', 'github']:
        return redirect('login')

    form = NicknameForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)

        if oauth == 'naver':
            profile = get_naver_profile(access_token)
        else:
            profile = get_github_profile(access_token)

        email = profile.get('email')

        if User.objects.filter(email=email).exists():
            raise Http404

        user.email = email
        user.is_active = True
        # user.set_password(User.objects.make_random_password()) # error
        user.set_password('ddddd') # 임시
        user.save()

        login(request, user)
        return redirect('main')
    return render(request, 'auth/nickname.html', {'form': form})

def get_naver_access_token(code, state):
    params = {
        'grant_type': 'authorization_code',  # 발급
        'client_id': settings.NAVER_CLIENT_ID,
        'client_secret': settings.NAVER_SECRET,
        'code': code,
        'state': state
    }

    response = requests.get(NAVER_TOKEN_URL, params=params)
    result = response.json()
    return result.get('access_token')


def get_naver_profile(access_token):
    # 회원정보 요청 (oauth로 받은 token과 같이 재요청)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # 회원정보 응답
    response = requests.get(NAVER_PROFILE_URL, headers=headers)

    if response.status_code != 200:
        raise Http404

    result = response.json()

    return result.get('response')


def get_github_access_token(code, state):
    params = {
        'grant_type': 'authorization_code',  # 발급
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_SECRET,
        'code': code,
        'state': state
    }

    response = requests.get(GITHUB_TOKEN_URL, params=params)
    # print(response)
    # print(response.content)
    response_str = response.content.decode()
    response_dict = parse_qs(response_str)
    access_token = response_dict.get('access_token', [])[0]

    return access_token


def get_github_profile(access_token):
    # 회원정보 요청 (oauth로 받은 token과 같이 재요청)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # 회원정보 응답
    response = requests.get(GITHUB_PROFILE_URL, headers=headers)

    if response.status_code != 200:
        raise Http404

    result = response.json()

    if not result.get('get'):
        result['email'] = f'{result['login']}@id.github.com'

    print('*'*100)
    print(result)
    print('*' * 100)

    return result