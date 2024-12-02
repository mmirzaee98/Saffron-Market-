from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Blog, BlogComment
from shop.models import Product, ProductComment
from .serializers import BlogSerializer, ProductSerializer, BlogCommentSerializer, ProductCommentSerializer

# these classes are logic that what each views return
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'publish', 'date_create']

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price', 'creator', 'off_percentage']

class AllBlogCommentsView(generics.ListAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'blog', 'rate', 'date']

class AllProductCommentsView(generics.ListAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product', 'rate', 'date']

class CreateBlogCommentView(generics.CreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class CreateProductCommentView(generics.CreateAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer