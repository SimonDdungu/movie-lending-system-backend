from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'phonenumber', 'NIN', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']