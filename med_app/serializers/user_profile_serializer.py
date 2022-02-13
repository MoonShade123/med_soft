from rest_framework import serializers

from med_app.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'middle_name', 'birth_date', 'weight', 'height', 'country', 'med_insurance', 'sex')

# class UserListProfileSerializer(serializers.ListSerializer):
#    child = UserProfileSerializer()
#    allow_null = True
#    many = True
