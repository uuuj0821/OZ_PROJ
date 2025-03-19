from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


# FBV-blog_list(request)와 동일
class BlogListView(ListView):
    # model = Blog => Blog.objects.all() 과 같음 // order_by() 등 함수사용 시 아래와 같이 작성
    # queryset = Blog.objects.all().order_by('-created_at') # 혹은 ordering 변수로 선언할 수 있음
    queryset = Blog.objects.all()
    ordering = ('-created_at',)
    template_name = 'blog_list.html'
    paginate_by = 10
    # for문에 들어가는 model 데이터들을 obejct_list 라는 변수명으로 받는다.
    # 그래서 object_list 변수명을 사용해야 함!!
    # blog_list.html에서 'page_object' 변수를 사용 했던것을 -> 'object_list'로 변경해야함!

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )

        return queryset


# FBV-blog_detail와 동일
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'CBV'

        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(id__lte=50)

    # def get_object(self, queryset=None):
    #     object = super().get_object()
    #     # object = self.model.objects.get(pk=self.kwargs.get('pk')) # 위 라인과 유사 동작
    #
    #     return object

# FBV-blog_create와 동일
# LogiRequiredMixin = @login_required()
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ('category', 'title', 'content') # forms.py 대신으로 이렇게 사용함

    # success_url = reverse_lazy('blog_list') # 정적페이지로 갈 때는 함수보다 이렇게 사용하는게 용이함
    # success_url = reverse_lazy('cb_blog_detail', kwargs={'pk':object.pk}) # 매개변수가 필요한 경우 이렇게 사용할 수 없다. 오류 뜸 / 함수로 작성해줘야 함(get_success_url 참조)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk':self.object.pk})


# FBV-blog_update와 동일
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ('category', 'title', 'content')


    # 동일 사용자 걸러내기
    # views.py의 blog_update()의 blog = get_object_or_404(Blog, pk=pk, author=request.user) 해당 라인과 동일 동작
    # 방법1 (코드가 짧아서 이걸 더 추천)
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:  # if 혹은 if not 사용으로 분리해주면 됨
            return queryset # superuser면 전체 쿼리 반환
        return queryset.filter(author=self.request.user) # superuser 아니면 해당 user 정보의 쿼리만 출력

    # # 방법2
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.author != self.request.user:
    #         raise Http404
    #     return self.object
    # 동일 사용자 걸러내기_end

    # 아래의 get_success_url() 함수가 없을 경우 models.py의 get_absolute_url() 함수를 호출한다.
    # def get_success_url(self):
    #     return reverse_lazy('cb_blog_detail', kwargs={'pk':self.object.pk})

# FBV-blog_delete와 동일
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser: # if 혹은 if not 사용으로 분리해주면 됨
            return queryset.filter(author=self.request.user)
        return queryset

        # 코드 작성의 팁
        '''
        if 보다는 if not을 쓰는것을 추천
        나중에 코드가 길어지면 if는 복잡 + 가독성이 떨어질 수 있음
        if a:
            if b:
                if c:
        와 같은 구조를 만들 수 있음
        '''

    def get_success_url(self):
        return reverse_lazy('blog:list')