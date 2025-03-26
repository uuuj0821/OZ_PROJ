from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from post.forms import CommentForm
from post.models import Comment, Post


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    # 유저정보가 필요하기 때문에 바로 저장하면 안되고 아래와 같이 유저정보 저장 후 저장
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        self.object.post = post
        self.object.save()

        return HttpResponseRedirect(reverse('main'))