from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from med_app.models import Profile
from med_app.serializers import UserProfileSerializer


class UserProfileAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = request.user
        profile = get_object_or_404(Profile.objects.all(), user=user)
        serializer = UserProfileSerializer(profile).data
        return Response(serializer)

    def post(self, request):
        profile = request.data
        user = request.user
        for i in profile:
            if i == 'name' is None:
                return Response('You must enter your name', 404)
            if i == 'surname' is None:
                return Response('You must enter your surname', 404)
            if i == 'birth_date' is None:
                return Response('You must enter your birth date', 404)
            if i == 'weight' is None:
                return Response('You must enter your weight', 404)
            if i == 'height' is None:
                return Response('You must enter your height', 404)
            if i == 'med_insurance' is None:
                return Response('You must enter your medical insurance', 404)
            if i == 'sex' is None:
                return Response('You must enter your sex', 404)

        new_profile = Profile.objects.get(user=user)
        if new_profile is None:
            new_profile = Profile.objects.create(user=user, name=profile['name'], surname=profile['surname'],
                                                 birth_date=profile['birth_date'], weight=profile['weight'],
                                                 height=profile['height'], med_insurance=profile['med_insurance'],
                                                 sex=profile['sex'])
        else:
            return Response(f'Profile for User: {user.username} already existing', 400)

        new_profile.save()

        serializer = UserProfileSerializer(new_profile).data

        return Response(serializer)

    def put(self, request):
        update_profile = request.data
        user = request.user
