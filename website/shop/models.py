from django.db import models
from tinymce.models import HTMLField


# Model for handling product data
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    content = HTMLField()
    price = models.PositiveIntegerField(default=0, help_text="based on USD")
    image = models.ImageField(upload_to="product")
    views = models.PositiveIntegerField(default=0)
    off_percentage = models.PositiveIntegerField(default=0)
    category = models.ForeignKey("shop.Category", on_delete=models.CASCADE)
    creator = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    owner = models.CharField(max_length=150)
    date_create = models.DateField(auto_now_add = True)
    date_update = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
    
# Model for handling category data
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name
    
# Model for handling product comments data
class ProductComment(models.Model):
    user = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.PositiveIntegerField(default=3)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

# Model for handling Invoices data
class Invoice(models.Model):
    user = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add = True)
    description = models.TextField()
    send_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
    