"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from member import views as member_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # blog
    path('', views.blog_list, name="blog_list"),
    path('<int:pk>/', views.blog_detail, name="blog_detail"),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),


    # auth
    path('accounts/', include("django.contrib.auth.urls")), # logi, logout 외에 다른거 사용용
    path('login/', member_views.login, name='login'),
    path('logout/', member_views.logout, name='logout'),
    path('signup/', member_views.sign_up, name="sign_up"),
]

# path 옵션에 name을 작성해 놓으면, route가 변하더라도 .html 에서는 name 값을 불러오면 되기 때문에 유지보수면에서 아주 용이하다.
# route가 변경되어도 이외에 수정해야할 부분이 없음
# 예를 들어 .html에 <a href="blog/{{ blog.pk }}" ~ 이런식으로 되어있으면 일일이 경로를 수정해 줘야 함
# 근데 <a href="{% url 'blog_detail' blog.pk %}"> 해놓으면 별다른 수정을 안 해줘도 됨
