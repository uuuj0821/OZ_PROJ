from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Blog
from django.conf import settings

# 뷰 로직에 문제가 없는지 테스트
class BlogViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test',
            is_active=True
        )

        Blog.objects.create(
            title='배포',
            content='본문',
            author=user,
        )

        future_published_at = timezone.now() + timedelta(days=30)
        Blog.objects.create(
            title='아직 배포 안 됨',
            content='본문',
            author=user,
            published_at=future_published_at
        )

    # 앞에 무조건 test_ 로 시작해야 함
    def test_blog_list(self):
        response = self.client.get(reverse('blog_list'))
        blog_list = Blog.objects.all()

        # status code
        self.assertEqual(response.status_code, 200)

        # context
        self.assertEqual(response.context.get('blog_list').count(), blog_list.count())

    def test_blog_create_not_login(self):
        response = self.client.get(reverse('blog_create'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], settings.LOGIN_URL + '?next=/create/')

    def test_blog_create(self):
        user = User.objects.first()
        self.client.force_login(user)

        blog_count = Blog.objects.count()

        # published_at = null 인 경우
        response = self.client.post(
            reverse('blog_create'),
            data={
                'title':'제목',
                'content':'본문',
                'published_at': ''
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('blog_list'))
        self.assertEqual(blog_count + 1, Blog.objects.all().count())


        # published_at = future 인 경우
        all_count = Blog.all_objects.count()
        self.client.post(
            reverse('blog_create'),
            data={
                'title': '제목',
                'content': '본문',
                'published_at': timezone.now() + timedelta(days=2)
            }
        )
        self.assertEqual(blog_count + 1, Blog.objects.all().count())
        self.assertEqual(all_count + 1, Blog.all_objects.count())


        # published_at 현재보다 작은 경우
        all_count = Blog.all_objects.count()
        self.client.post(
            reverse('blog_create'),
            data={
                'title': '제목',
                'content': '본문',
                'published_at': timezone.now() - timedelta(days=2)
            }
        )
        self.assertEqual(blog_count + 2, Blog.objects.all().count())