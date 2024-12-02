from django.db import models


# model for handling contact form data
class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    text = models.TextField()

    def __str__(self):
        return self.name
    