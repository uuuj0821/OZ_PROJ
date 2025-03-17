from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def index(request):
    return HttpResponse('Hello World!')

def blog_list(request):
    blogs = Blog.objects.all()
    visits = int(request.COOKIES.get('visits', 0)) + 1
    # COOKIES에 'visits' 가 없으면 0으로 받고 + 1 해줌 / 있으면 visits 값 불러옴
    # return 값이 string이라서 int로 형변환 해줌
    # 쿠키는 브라우저에 저장을 하기 때문에 보안에 문제가 되는 중요한 정보는 담아서는 안 된다!!!! 개발자 도구를 통해서 확인을 할 수 가 있으므로!

    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        'blogs': blogs,
        'count': request.session['count']
    }

    response = render(request, 'blog_list.html', context)
    response.set_cookie('visits', visits)

    return response

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    context = {
        'blog' : blog
    }

    return render(request, 'blog_detail.html', context)

