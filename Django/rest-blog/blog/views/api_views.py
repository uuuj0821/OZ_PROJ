from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import schema, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        blog_list = Blog.objects.all().order_by('-created_at').select_related('author')
        paginator = PageNumberPagination()
        queryset = paginator.paginate_queryset(blog_list, request)

        serializer = BlogSerializer(queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)

            # 기존방식 - 안먹힘(why? commit=False를 사용할 수 없다.) / 위와 같이 작성
            # blog = serializer.save(commit=False)
            # blog.author = request.user
            # blog = serializer.save()
            # 기존방식 - 안먹힘_end

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CBV
class BlogDetailAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        blog_list = Blog.objects.all().select_related('author')
        pk = kwargs.get('pk', 0)

        # 방법1
        # blog = blog_list.filter(pk=pk).first()
        # if not blog:
        #     from django.http import Http404
        #     raise Http404

        # 방법2
        blog = get_object_or_404(blog_list, pk=pk)

        serializer = BlogSerializer(blog, many=False)
        return Response(serializer.data)


# FBV
@api_view(['GET'])
@schema(AutoSchema())
def detail_view(request, pk):
    blog_list = Blog.objects.all().select_related('author')
    blog = get_object_or_404(blog_list, pk=pk)

    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


# CBV, FBV 비교
# GET요청 외에도 POST, PUT, PATCH, DELETE가 있는데
# CBV의 경우에는 클래스 내부에 def get(), def post(), def put() 등으로 작성할 수 있음
# 근데 FBV의 경우에는 아래와 같이 작성된다. 그래서 CBV를 더 권장한다.
'''
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@schema(AutoSchema())
def detail_view(request, pk):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass
'''

