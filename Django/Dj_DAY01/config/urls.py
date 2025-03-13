"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render, redirect
from pprint import pprint ## 매개변수 reqeust.__dict__ 출력용

"""
* 매개변수 request *
매개변수 request 란? 클라이언트의 요청 정보들이 담겨있음.
예를 들어, method=get, path=/user/, user 정보(id, password), 쿠키정보 등
근데, print(request)를 할 경우 기본적으로 __str__ 함수에 의해 method, path만 확인이 가능
이외의 정보를 확인하려면 request,__dict__ 를 통해 전체 정보를 확인 할 수 있다.
단, print(request.__dict__) 할 경우 가독성이 굉장히 떨어진다. => 한 줄로 출력됨
가독성을 높여 출력하는 방식으로는
 1. json.dumps()
 2. pprint()
 3. for문 출력
"""

## ------------------------------------------------------------- 1-6. 간단한 http 응답 만들어보기 & 1-9. template 이용한 페이지 만들기

def index(request): ## 단순 Hello world 텍스트를 웹 브라우저에 출력
    print("request : ", request) ## request argument 정보 확인용
    pprint(request.__dict__) ## request argument 정보 확인용
    return HttpResponse("<h1>Hello world</h1>") ## 단순 Hello world 텍스트를 웹 브라우저에 출력

## HttpResponse() 함수의 사용 (HttpResponse() vs render() 코드 하단에 정리함!)
##  - 간단한 텍스트 출력용으로 사용하면 좋음
"""
def book_list(request):
    book_text = ''

    for i in range(0, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지 입니다.'
    return HttpResponse(book_text)
"""

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지 입니다.')

def python(request):
    return HttpResponse('python 페이지 입니다.')


## render() 함수 사용 (+ templates(.html) 파일들 필수)
def book_list(request):
    return render(request, 'book_list.html', {'range':range(0, 10)})

def book(request, num):
    return render(request, 'book_detail.html', {'num':num})


## ------------------------------------------------------------- 1-7. 가짜 db & 1-9. template 이용한 페이지 만들기

movie_list = [
    {"title":"파묘", "director":"장재현"},
    {"title":"웡카", "director":"폴 킹"},
    {"title":"듄: 파트 2", "director":"드니 빌뇌브"},
    {"title":"시민덕희", "director":"박영주"}
]


## 항상 리스트 컴프리헨션의 방법을 쓰진 않는다. 간결하게 코드 작성할 수 있는 경우에 많이 쓰지
## 복잡한 로직에서는 가독성을 위해 오히려 for문을 많이 사용!
def movies(request):
    ## 기본 텍스트만 출력 실습 - 리스트 컴프리헨션 + HttpResponse() 함수 사용의 경우
    """
    movie_titles = [movie['title'] for movie in movie_list] # 리스트 컴프리헨션
    response_text = '<br>'.join(movie_titles) # html 줄바꿈(<br>으로 문자열 결합

    return HttpResponse(response_text)
    """

    ## 영화 타이틀 하이퍼링크를 추가하여 해당 detail 화면으로 넘어가도록 하기 실습 1
    """
    movie_titles = [movie['title'] for movie in movie_list]
    response_text = ''

    for i, movie_title in enumerate(movie_titles):
        response_text += f'<a href="/movie/{i}/"> {movie_title} </a><br>'

    return HttpResponse(response_text)
    """

    ## 영화 타이틀 하이퍼링크를 추가하여 해당 detail 화면으로 넘어가도록 하기 실습 2 - 리스트컴프리헨션으로 코드 더 간결하게 해보기
    ## 위 실습1과 실행은 동일함. 단, 코드만 간결해진것 뿐
    """
    movie_titles = [f'<a href="/movie/{i}/"> {movie['title']} </a><br>'
                    for i, movie in enumerate(movie_list)]
    response_text = ''.join(movie_titles)

    return HttpResponse(response_text)
    """

    ## render() 함수 사용 (+ templates(.html)
    ## render() 함수 사용 시 (from django.shortcuts import render)
    return render(request, 'movies.html', {'movie_list': movie_list})
    ## settings.py에 templates 폴더 경로 추가 해줘야함!!
    ## 혹은 명시적으로 작성가능(콜론이 아닌 =로 작성해야함!!)
       ## return render(request, template_name='movies.html', context={'movie_list': movie_list})


def movie_detail(request, index):
    ## HttpResponse() 함수 사용 실습
    """
    if index > len(movie_list)-1:
        return HttpResponse("잘못된 주소입니다.") # 혹은 raise Http404 에러를 강제발생시킴 (from django.http import Http404 필요)
        # 위에서 index 초과된 값을 넣으면 500번대 에러가 뜨는데 500번대 에러는 서버의 잘못인 경우 발생하는 에러
        # 400번대는 클라이언트 실수에 의한 에러 이므로 404 에러를 발생시키도록 한다.

    movie = movie_list[index]
    movie_info = f'<h1>영화제목 : {movie["title"]}</h1> <p>영화감독 : {movie["director"]}</p>'
    return HttpResponse(movie_info)
    """

    ## render() 함수 사용 실습
    if index > len(movie_list) - 1:
        return HttpResponse("잘못된 주소입니다.")

    movie = movie_list[index]
    return render(request, 'movie.html', {'movie':movie})


## ------------------------------------------------------------- 1-10. 구구단

def gugudan(request, num):
    """
    # 구구단은 2 ~ 9단 까지
    if num < 2:
        num = 2

    # if num > 9:
    #     num = 9

    result = list()

    for i in range(1, 10):
        result.append(num * i)

    return render(request, 'gugudan.html',
                  {'num':num, 'result':result})
    """

    # 리스트컴프리헨션 사용 + 전달변수 context로 만듦
    if num < 2:
        return redirect('/gugudan/2')
        # num = 2 # 2라고 하는 것 보다는 redirect() 함수를 쓰는게 좋다.
        """
        이유는? 예로 0, 1 로 접속할 경우 uri는 /0, /1로 표시가 되는데
        아래의 내용은 2단으로 표시가 된다. 그래서 이것보다는 redirect(path정보)를 해서 2단 페이지로 출력되도록 응답한다.
        """

    context = {
        'num': num,
        'result': [num * i for i in range(1, 10)]
    }

    return render(request, 'gugudan.html', context)




# path 마지막에 항상 / 붙여줘야함!***** 장고의 특성임!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('python/', python), ## python 호출의 경우, 해당 라인이 출력 되는게 아니라 위의 str에 우선 걸리기 때문에 위의 라인이 출력 됨. 그래서 str 사용 시 웬만하면 제일 하단에 쓸 것. 근데 str은 잘 사용하지는 않음.
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugudan/<int:num>/', gugudan),
]


"""
* HttpResponse() 함수 사용의 경우
 - 기능 : 함수 내에서 html 코드를 작성한 후 HttpResponse()를 통해 웹 브라우저에 출력 해 줌
 - 장점 : 간단한 내용을 작성하고 출력할 때는 용이하다. 
         함수내에서 html 내용을 작성한 후 HttpResponse() 에 담아주고 실행시키면 바로 웹 브라우저에서 확인 가능함
 - 단점 : html 내용이 길어지면 코드의 가독성이 떨어지고 지저분해진다.
         코드 유지/보수 면에서도 어려움
         
* render() 함수 사용의 경우
 - 기능 : 필요한 데이터를 가공하고 특정 .html 파일로 전달하여 웹 브라우저에 출력 할 수 있도록 함
 - 장점 : 실제 동작?부분 함수 혹은 파일 (views.py, urls.py, ...)들이 깔끔하고 가독성이 올라감
         url, view, html 등으로 파일을 분리하여 관리하기에 유지/보수성이 좋음
 - 단점 : 이 있나?? 
"""