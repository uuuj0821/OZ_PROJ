from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.decorators.http import require_http_methods

from blog.forms import BlogPostForm
from blog.models import Blog

def index(request):
    return HttpResponse('Hello World!')

# 방문자 테스트용
# def blog_list(request):
#     blogs = Blog.objects.all().order_by('-created_at') # - : desc 정렬 // 'created' 하면 asc 정렬임
#     visits = int(request.COOKIES.get('visits', 0)) + 1
#     # COOKIES에 'visits' 가 없으면 0으로 받고 + 1 해줌 / 있으면 visits 값 불러옴
#     # return 값이 string이라서 int로 형변환 해줌
#     # 쿠키는 브라우저에 저장을 하기 때문에 보안에 문제가 되는 중요한 정보는 담아서는 안 된다!!!! 개발자 도구를 통해서 확인을 할 수 가 있으므로!
#
#     request.session['count'] = request.session.get('count', 0) + 1
#
#     context = {
#         'blogs': blogs,
#         'count': request.session['count']
#     }
#
#     response = render(request, 'blog_list.html', context)
#     response.set_cookie('visits', visits)
#
#     return response

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at') # - : desc 정렬 // 'created' 하면 asc 정렬임

    q = request.GET.get('q')
    if q:
        # 제목, 본문에서 검색
        blogs = blogs.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )

        # blogs = blogs.filter(title__icontains=q) # 제목 검색
        # blogs = blogs.filter(content__icontains=q) # 본문내용 검색

    # 페이지네이션
    paginator = Paginator(blogs, 10) # 한페이지당 몇개씩
    page = request.GET.get('page') # 현재페이지 값
    page_object = paginator.get_page(page)
    # 페이지네이션_end

    context = {
        'object_list': page_object.object_list,
        'page_obj': page_object,
    }

    return render(request, 'blog_list.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    context = {
        'blog' : blog,
        'test' : 'TEST'
    }

    return render(request, 'blog_detail.html', context)


# 블로그 글 생성 페이지
@login_required()
def blog_create(request):
    # 데코레이터 login_required() 로 대체 가능함
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))

    form = BlogPostForm(request.POST or None)

    if form.is_valid(): # post의 경우 -> 유효성 검사 통과의 경우 if 실행 // get의 경우에는 if문 false
        blog = form.save(commit=False) # form 에 작성한 내용 저장 // commit=False를 하면 모델 생성은 하고 db에 저장은 안 함
        blog.author = request.user # blog.author 정보는 현재 접속한 user 정보
        blog.save() # 윗줄에서 author 정보 담아준 후 다시 저장

        '''
        저장 및 생성 완료 하면 blog_detail 페이지로 redirect
        단, blog_detail은 pk 값을 가짐, form.save() 하면서 속성값들이 저장되니까 그걸 변수로 담아서 가져옴
        
        ** reverse()는 url을 동적으로 생성하는 함수임, 이때 url 패턴에 동적으로 전달해야할 인자가 있으면
           kwargs를 사용해주어야 한다.
        '''
        return redirect(reverse('fb:detail', kwargs={'pk':blog.pk}))

    context = {'form': form}

    return render(request, 'blog_form.html', context)

# 블로그 글 수정하기
@login_required()
def blog_update(request, pk):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, pk=pk)
    else:
        blog = get_object_or_404(Blog, pk=pk, author=request.user)

    form = BlogPostForm(request.POST or None, request.FILES or None, instance=blog)
    print(request.POST, request.FILES)

    if form.is_valid():
        print(form.cleaned_data)
        blog = form.save()
        return redirect(reverse('fb:detail', kwargs={'pk': blog.pk}))

    context = {
        'blog':blog,
        'form': form
    }

    return render(request, 'blog_form.html', context)

# 블로그 글 삭제하기
@login_required()
@require_http_methods(['POST'])
def blog_delete(request, pk):
    # 아래 라인 대신에 @require_http_methods(['POST'])
    # if request.method != "POST":
    #     raise Http404

    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()

    return redirect(reverse('fb:list'))


