from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Blog, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True) # fk
    comment_count = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.comment_set.count()

    def get_author_name(self, obj):
        return obj.author.username


    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author',
                  'published_at', 'created_at', 'updated_at', 'comment_count', 'author_name']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content']

class CommentUpdateSerializer(CommentSerializer):
    blog = BlogSerializer(many=False, read_only=True)

    # 상속받아도 meta는 안 가져오기 때문에 작성해줘야 함
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'blog']