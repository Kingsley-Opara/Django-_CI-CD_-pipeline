from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Blog(models.Model):
    status_choices = (
        ("draft", "Draft"),
        ("publish", "Publish")

    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=250)
    discription = models.CharField(max_length=250)
    status = models.CharField(max_length=100, choices=status_choices, default="draft")
    content = models.TextField()
