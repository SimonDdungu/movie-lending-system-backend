import uuid
from django.db import models

# Create your models here.

class Movies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    studio = models.CharField(max_length=255, blank=True, null=True)
    release_year = models.IntegerField()
    cover = models.ImageField(upload_to="movie_covers/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

