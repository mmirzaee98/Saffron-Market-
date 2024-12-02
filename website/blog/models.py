from django.db import models
from tinymce.models import HTMLField


# Model for handling blog data
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="blog")
    author = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    content = HTMLField()
    view = models.IntegerField(default=0)
    date_create = models.DateField(auto_now_add = True)
    date_update = models.DateField(auto_now = True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# model for handling blog comments data
class BlogComment(models.Model):
    user = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    text = models.TextField()
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=3)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


