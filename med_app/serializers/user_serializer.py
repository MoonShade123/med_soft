from rest_framework import serializers

from med_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'is_active')


class UserListSerializer(serializers.ListSerializer):
    child = UserSerializer()
    allow_null = True
    many = True