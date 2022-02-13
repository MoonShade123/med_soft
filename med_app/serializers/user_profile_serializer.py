from rest_framework import serializers

from med_app.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# class UserListProfileSerializer(serializers.ListSerializer):
#    child = UserProfileSerializer()
#    allow_null = True
#    many = True
