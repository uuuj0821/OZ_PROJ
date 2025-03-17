from django.db import models

class Blog(models.Model):
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
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES)
    # category가 CharField로 만들어졌지만 choices 옵션으로 인해서 콤보 박스 형태로 노출 됨!

    # author = models.CharField('작성자', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:20]}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'




# 1. 모델을 작성하기에 앞서, 해당 프로젝트 별 필요로 한게 무엇인지 생각해보기.
# 예) 블로그에 필요한 요소들
'''
제목, 본문, 작성자, 작성일자, 수정일자, 카테고리, ...
'''
