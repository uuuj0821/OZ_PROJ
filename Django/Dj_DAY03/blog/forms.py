from django import forms
from blog.models import Blog

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__' # 전부 가져오고 싶을 때
        fields = ('title', 'content')