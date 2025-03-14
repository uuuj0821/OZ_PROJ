from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from Dj_DAY02.models import Bookmark


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50) # id가 50 이상인 애들만 조회

    context = {
        'bookmarks': bookmarks,
    }
    # return HttpResponse('<h1>북마크 리스트 페이지입니다.</h1>')
    return render(request, 'bookmark_list.html', context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     raise Http404

    # try-except 문과 동일하게 작용 함
    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark':bookmark}

    return render(request, 'bookmark_detail.html', context)