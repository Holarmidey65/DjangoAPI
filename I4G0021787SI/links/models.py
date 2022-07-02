from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField()

