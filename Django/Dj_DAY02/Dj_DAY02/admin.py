from django.contrib import admin
from Dj_DAY02.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url'] # 화면에 이름, url로 구분 후 표시
    list_display_links = ['name', 'url'] # 이름, url에 하이퍼링크 추가 (해당 설정으로 접속한다.)
    list_filter = ['id', 'name', 'url']

# 위와 같은 기능을 함
"""
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url'] # 화면에 이름, url로 구분 후 표시
    list_display_links = ['name', 'url'] # 이름, url에 하이퍼링크 추가 (해당 설정으로 접속한다.)

admin.site.register(Bookmark, BookmarkAdmin)
"""
