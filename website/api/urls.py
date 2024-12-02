from django.urls import path
from .views import BlogListView, ProductListView, AllBlogCommentsView, AllProductCommentsView, CreateBlogCommentView, CreateProductCommentView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # API Endpoints
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('blogs/comments/', AllBlogCommentsView.as_view(), name='blog-comments'),    
    path('products/comments/', AllProductCommentsView.as_view(), name='products-comments'),
    path('blogs/comments/create/', CreateBlogCommentView.as_view(), name='create-blog-comment'),
    path('products/comments/create/', CreateProductCommentView.as_view(), name='create-product-comment'),   

    # OpenAPI schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Redoc UI
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
