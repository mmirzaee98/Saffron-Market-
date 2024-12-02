"""
URL configuration for zafaran project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from blog.views import blog, blogs
from main.views import contact, about, home, terms, faq
from shop.views import checkout, shop, product
from user.views import receipt, signin, signup, my_account, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    # blog
    path('blog/<int:pk>/', blog, name="Blog"),
    path('blogs/', blogs, name="Blogs"),

    # main
    path('contact/', contact, name="Contact"),
    path('about/', about, name="About"),
    path('', home, name="Home"),
    path('terms/', terms, name="Terms"),
    path('faq/', faq, name="FAQ"),

    # shop
    path('shop/', shop, name="Shop"),
    path('product/<int:pk>/', product, name="Product"),
    path('checkout/', checkout, name="Checkout"),

    # user
    path('receipt/', receipt, name="Receipt"),
    path('signin/', signin, name="SignIn"),
    path('signup/', signup, name="SignUp"),
    path("logout/", logout, name="Logout"),
    path('my-account/', my_account, name="MyAccount"),

    path('api/', include('api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
