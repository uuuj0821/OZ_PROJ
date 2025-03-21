from django.contrib import admin
from blog.models import Blog, Comment

admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['content', 'author']
    extra = 1  # 기본이 3개인듯? 댓글 작성할 수 있는 창이 3개가 나와있어서 extra=1 로 선언하여 1개만 출력되도록 함

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
