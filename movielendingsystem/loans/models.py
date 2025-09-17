import uuid
from django.db import models
from movies.models import Movies
from users.models import Users


class Loans(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, related_name="loans")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="loans")
    movie_title = models.CharField(max_length=255)
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

