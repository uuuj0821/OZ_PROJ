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

movie_list = [
    {"title":"파묘", "director":"장재현"},
    {"title":"웡카", "director":"폴 킹"},
    {"title":"듄: 파트 2", "director":"드니 빌뇌브"},
    {"title":"시민덕희", "director":"박영주"}
]

def index(request):
    return HttpResponse("<h1>Hello world</h1>")

# def book_list(request):
#     book_text = ''
#
#     for i in range(0, 10):
#         book_text += f'book {i}<br>'
#
#     return HttpResponse(book_text)

# def book(request, num):
#     book_text = f'book {num}번 페이지 입니다.'
#     return HttpResponse(book_text)

## templates 사용
def book_list(request):
    return render(request, 'book_list.html', {'range':range(0, 10)})

def book(request, num):
    return render(request, 'book_detail.html', {'num':num})

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지 입니다.')

def python(request):
    return HttpResponse('python 페이지 입니다.')

def movies(request):
    ## 리스트 컴프리헨션 사용
    # movie_titles = [movie['title'] for movie in movie_list]

    ## 위 한 줄과 동일
    # movie_titles = []
    # for movie in movie_list:
    #     movie_titles.append(movie['title'])

    # response_text = '<br>'.join(movie_titles)

    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie["title"]}</a>'
    #     for index, movie in enumerate(movie_list)
    # ]
    #
    # response_text = '<bt>'.join(movie_titles)
    #
    # return HttpResponse(response_text)

    ## views 대신 templates 사용하는 방법
    return render(request, 'movies.html', {'movie_list':movie_list})

def movie_detail(request, index):
    if index > (len(movie_list)-1) :
        raise Http404 ## 404 에러 강제로 출력 해줌

    movie = movie_list[index]
    # response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
    # return HttpResponse(response_text)

    ## templates 방법
    movie = movie_list[index]
    context = {'movie':movie}
    return render(request, 'movie.html', context)


# ----------------------------------- 구구단

def gugudan(request, num):
    if num < 2:
        return redirect('/gugudan/2/')

    context = {
        'num':num,
        'results':[num * i for i in range(1, 10)]
    }

    return render(request, 'gugudan.html', context)


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
