from django.db import models
# model = db의 테이블과 같다.
# field = db의 컬럼과 같다.

# 북마크
# - 이름 : varchar
# - url주소 : varchar

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

# 이런식으로 여러개의 테이블을 만들 수 있다.
class BookmarkCategory(models.Model):
    pass


# 1단계
# makemigrations => migration.py 파일을 만듦
# 실제 db에는 영향 x => 실제 db에 넣기위한 정의를 하는 파일을 생성 / db에 적용이 되진 않음
# git과 비교하여 commit과 같은 동작이라고 볼 수 있음 => github에 적용이 되진 않음
#
# 2단계
# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 db에 적용함
# git과 비교하여 push와 같은 동작이라고 볼 수 있음 => github에 적용이 됨



