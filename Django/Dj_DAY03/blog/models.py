from django.db import models
from django.urls import reverse

# 커스텀user와 충돌이 발생할 수 있으므로 import user보다는
# AbstractUser + get_user_model()을 사용하는게 용이
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from utils.models import TimeStampedModel

User = get_user_model() # 장고에서 현재 설정된 User 모델(기본User, 커스텀User)을 자동으로 가져오도록 변경!

class Blog(TimeStampedModel):
    CATEGORY_CHOICES = (
        # ('db에 들어갈 카테고리명', '블로그상에서 보여질 카테고리명')
        ('python', 'python 학습'),
        ('db', 'db 학습'),
        ('aws', 'aws 학습'),
        ('django', 'django 학습'),
        ('error', 'error 모음')
    )

    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES, default='django')
    # category가 CharField로 만들어졌지만 choices 옵션으로 인해서 콤보 박스 형태로 노출 됨!

    author = models.ForeignKey(User, on_delete=models.CASCADE) # 참조무결성
    # models.CASCADE : 같이 삭제 됨
    # models.PROTECT : 삭제 불가능 (user를 삭제하려고 할 때 블로그가 있으면 user 삭제 불가능)
    # models.SET_NULL : NULL 값으로 대체 (유저 삭제 시 블로그의 author가 null이 됨) / 이때 매개변수로 null=True 도 추가해 줘야 함

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:20]}'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_pk':self.pk})

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

# 1. 모델을 작성하기에 앞서, 해당 프로젝트 별 필요로 한게 무엇인지 생각해보기.
# 예) 블로그에 필요한 요소들
'''
제목, 본문, 작성자, 작성일자, 수정일자, 카테고리, ...
'''


class Comment(TimeStampedModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField('본문', max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} 댓글'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'
        ordering = ('-created_at', '-id')


    '''
    어떤 블로그글에 달릴지
    댓글 내용
    작성자
    작성일자
    수정일자
    '''
