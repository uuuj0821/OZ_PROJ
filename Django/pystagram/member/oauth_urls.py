from django.urls import path
from . import oauth_views

app_name = 'oauth'

urlpatterns = [
    # NAVER
    path('naver/login/', oauth_views.NaverLoginRedirectView.as_view(), name='naver_login'),
    path('naver/callback/', oauth_views.naver_callback, name='naver_callback'),

    # GITHUB
    path('github/login/', oauth_views.GithubLoginRedirectView.as_view(), name='github_login'),
    path('github/callback/', oauth_views.github_callback, name='github_callback'),

    # common
    path('nickname/', oauth_views.oauth_nickname, name='nickname'),
]
