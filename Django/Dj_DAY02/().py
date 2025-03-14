# coding: utf-8
Bookmark.objects.all()
Bookmark.objects.get(id=2)
Bookmark.objects.get(id=3)
bookmark_list = Bookmark.objects.all()
bookmark_list[0]
Bookmark.objects.first()
Bookmark.objects.first().id
Bookmark.objects.last().id
Bookmark.objects.filter(id_gte=2)
Bookmark.objects.filter(id_gte=1)
Bookmark.objects.filter(id__gte=1)
Bookmark.objects.filter(id__gte=3)
Bookmark.objects.filter(id__gte=4)
Bookmark.objects.filter(id__gte=5)
Bookmark.objects.filter(id__lte=5)
Bookmark.objects.filter(name__icontains='네이')
Bookmark.objects.filter(name__startswith='네')
Bookmark.objects.filter(name__startswith='네이')
Bookmark.objects.filter(name__endswith='네이')
Bookmark.objects.filter(name__endswith='이버')
Bookmark.objects.filter(name__endswith='이')
Bookmark.objects.filter(name__in='이')
Bookmark.objects.filter(name__in=['이'])
Bookmark.objects.filter(name__in=['네이버'])
Bookmark.objects.all()
Bookmark.objects.filter(name='네이버', url_startswith='https://naver')
Bookmark.objects.filter(name='네이버', url__startswith='https://naver')
Bookmark.objects.create(name='야후', url='https://yahoo.com')
Bookmark.objects.all()
Bookmark.objects.get(name='네이버')
Bookmark.objects.get(name='네이버').url
bookmark = Bookmark(name='야후2', url='https://yahoo.com')
bookmark
bookmark.id
Bookmark.objects.all()
bookmark.save()
bookmark.id
Bookmark.objects.all()
b = _.first()
b
b.id
b.url
b.name
b.created_at
b.id =None
b.id
b.save()
b.id
Bookmark.objects.all()
b
b.name
b.name = "구글2"
b.name
b.save()
Bookmark.objects.all()
b.id
Bookmark.objects.filter(url__icontains='google.com')
Bookmark.objects.filter(url__icontains='google.com').update(name='구글')
Bookmark.objects.filter(url__icontains='google.com')
Bookmark.objects.filter(url__icontains='google.com').update(name='Google')
Bookmark.objects.filter(url__icontains='google.com')
b
b.id
b.delete()
b
b.id
Bookmark.objects.all()
Bookmark.objects.filter(name__icontains='야후')
Bookmark.objects.filter(name__icontains='야후').delete()
Bookmark.objects.filter(name__icontains='야후')
Bookmark.objects.all()
