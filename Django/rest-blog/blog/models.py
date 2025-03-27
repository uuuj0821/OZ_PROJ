from django.db.models import Manager, Q

from django.contrib.auth import get_user_model
from django.db import models
from utils.models import TimestampModel
from django.utils import timezone

User = get_user_model()

class PublishedManager(Manager):
    def get_queryset(self):
        now = timezone.now()

        return super().get_queryset().filter(
            Q(published_at__isnull=True) |
            Q(published_at__lte=now)
        )


class Blog(TimestampModel):
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField('배포일시', null=True, blank=True)

    objects = PublishedManager()
    all_objects = Manager()

    @property
    def is_active(self):
        now = timezone.now()

        if not self.published_at:
            return True

        return self.published_at <= now

    # 위와 같이 if문을 return 한줄로 작성 가능
    # def is_active(self):
    #     now = timezone.now()
    #     if self.published_at <= now:
    #         return True
    #     return False


    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'
        ordering = ['-created_at', '-id']