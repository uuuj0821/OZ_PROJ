from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.urls import reverse

# from config import settings
'''
1. from django.conf import settings : 현재 실행되고 있는 프로젝트의 환경의 setting을 알아서 찾아서 import 함
2. from config import settings : config 폴더에 있는 settings.py를 import 함

1, 2 import 하는 건 같지만,
2는 config 폴더명 혹은 settings.py 파일명이 변경되면 파일을 찾을 수가 없다.
그래서 웬만하면 1의 방식으로 import 하는 것을 추천 한다.
'''

def sign_up(request):
    # print(request.POST)

    # 방법1. 데이터가 없는 상태에서 get요청이 들어오면 에러가 발생할 수 있음
    '''
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    '''

    # 방법2. 방법1의 오류를 예방할 수는 있지만, user 정보에 대한 추후 작업을 할 때 불편함이 있음
    '''
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    print('username : ', username)
    print('password1 : ', password1)
    print('password2 : ', password2)
    '''

    # 방법3.
    # username 중복확인 작업
    # 패스워드가 맞는지, 그리고 패스워드 정책에 올바른지 (대소문자 등...)
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else: # get 요청일 때
        form = UserCreationForm() # 장고에서 기본적으로 제공해주는 form
    '''

    # 방법 4. 방법3의 축소 버전
    form = UserCreationForm(request.POST or None) # POST 이거나 get(아무것도 안 넣어줘도 되는 것)
    # request.POST => 방법3의 if request.method == 'POST': form = UserCreationForm(request.POST) 부분
    # request.GET => 방법3의 else : form = UserCreationForm() 부분

    # None일 경우 값이 없기 때문에 아래 if문은 진행하지 않고 넘어 감
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
        # return redirect('/accounts/login') # 이렇게 정적선언 하는 것보다 config/settings.py 에 변수로 담아서 불러오는 걸 추천


    # else:
    #     return HttpResponse('get요청')

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        django_login(request, form.get_user())
        # return redirect(settings.LOGIN_REDIRECT_URL) # config/settings.py에 선언된 변수의 url을 반환
        return redirect(reverse('blog_list')) # name을 입력해서 url을 반환 해줌

    context = {'form': form}

    return render(request, 'registration/login.html', context)

def logout(request):
    django_logout(request) # 사용자 세션 삭제 및 로그아웃 처리

    return redirect(settings.LOGOUT_REDIRECT_URL)
