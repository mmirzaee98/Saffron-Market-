from django.shortcuts import render
from blog.models import Blog


# This function renders a single blog page based on its primary key (pk) if it is published
def blog(request, pk):
    page = Blog.objects.get(pk=pk, publish=True)
    return render(request, 'blog.html', {'blog': page})

# This function renders a list of all published blogs
def blogs(request):
    objects = Blog.objects.filter(publish=True)
    return render(request, 'blogs.html',{'blogs':objects})
