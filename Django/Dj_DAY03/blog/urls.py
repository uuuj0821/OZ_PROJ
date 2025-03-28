from django.urls import path
from blog import cb_views
from blog import views

app_name = 'blog'
# 구조가 app_name:name 이런식 => blog:list
# 기존에는 blog_list 이렇게 작성한 것들 싹 바꿔줘야 함...

urlpatterns = [
    # CBV blog
    path('', cb_views.BlogListView.as_view(), name='list'),
    path('<int:pk>/', cb_views.BlogDetailView.as_view(), name='detail'),
    path('create/', cb_views.BlogCreateView.as_view(), name='create'),

    # cbv
    path('<int:pk>/update/', cb_views.BlogUpdateView.as_view(), name='update'),

    # fbv - 이미지 업로드 테스트용
    # path('<int:pk>/update/', views.blog_update, name='update'),


    path('<int:pk>/delete/', cb_views.BlogDeleteView.as_view(), name='delete'),
    path('comment/create/<int:blog_pk>/', cb_views.CommentCreateView.as_view(), name='comment_create'),
]

# {% url 'blog:list' %}