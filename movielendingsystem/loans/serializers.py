from rest_framework import serializers
from .models import Loans
from movies.serializers import MovieSerializer
from users.serializers import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    movies_id = serializers.UUIDField(write_only=True)
    users_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Loans
        fields = ['id', 'movie', 'user', 'borrow_date', 'due_date', 'returned_date', 'status', 'updatedAt' 'movies_id' 'users_id']
        read_only_fields = ['id', 'borrow_date', 'updatedAt']
