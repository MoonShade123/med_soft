from datetime import datetime

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

        try:
            new_profile = Profile.objects.get(user=user)
            return Response(f'Profile for User: {user.username} already existing', 400)
        except:
            new_profile = Profile.objects.create(user=user,
                                                 birth_date=datetime.today().strftime('%Y-%m-%d'))

            for key, value in profile.items():
                vars(new_profile)[key] = value

#        if profile['name'] is None:
#            return Response('You must enter your name', 404)
#
#        if profile['surname'] is None:
#            return Response('You must enter your surname', 404)
#
#        if profile['birth_date'] is None:
#            return Response('You must enter your birth_date', 404)
#
#        if profile['weight'] is None:
#            return Response('You must enter your weight', 404)
#
#        if profile['height'] is None:
#            return Response('You must enter your height', 404)
#
#        if profile['med_insurance'] is None:
#            return Response('You must enter your medical insurance', 404)
#
#        if profile['sex'] is None:
#            return Response('You must enter your sex', 404)
#
#        try:
#            new_profile = Profile.objects.get(user=user)
#            return Response(f'Profile for User: {user.username} already existing', 400)
#        except:
#            new_profile = Profile.objects.create(user=user, name=profile['name'], surname=profile['surname'],
#                                                 birth_date=profile['birth_date'], weight=profile['weight'],
#                                                 height=profile['height'], med_insurance=profile['med_insurance'],
#                                                 sex=profile['sex']
#                                                 )

        new_profile.save()

        serializer = UserProfileSerializer(new_profile).data

        return Response(serializer)

    def put(self, request):
        user = request.user
        update_profile = request.data

        saved_profile = get_object_or_404(Profile.objects.all(), user=user)

        if len(update_profile) is not 0:
            for key, value in update_profile.items():
                u = vars(saved_profile)
                u[key] = value
        else:
            return Response(f"No data provided to update User: {user.username} profile", 400)
#        for key, value in vars(saved_profile).items():
#            u = update_profile
#            u[key] = value
#        for key in update_profile:
#            if key == 'name' is not None:
#                saved_profile.name = update_profile['name']
#            else:
#                saved_profile.name = saved_profile.name
#            if key == 'surname' is not None:
#                saved_profile.surname = update_profile['surname']
#            else:
#                saved_profile.surname = saved_profile.surname
#            if key == 'middle_name' is not None:
#                saved_profile.middle_name = update_profile['middle_name']
#            else:
#                saved_profile.middle_name = saved_profile.middle_name
#            if key == 'birth_date' is not None:
#                saved_profile.birth_date = update_profile['birth_date']
#            else:
#                saved_profile.birth_date = saved_profile.birth_date
#            if key == 'weight' is not None:
#                saved_profile.weight = update_profile['weight']
#            else:
#                saved_profile.weight = saved_profile.weight
#            if key == 'height' is not None:
#                saved_profile.height = update_profile['height']
#            else:
#                saved_profile.height = saved_profile.height
#            if key == 'country' is not None:
#                saved_profile.country = update_profile['country']
#            else:
#                saved_profile.country = saved_profile.country
#            if key == 'med_insurance' is not None:
#                saved_profile.med_insurance = update_profile['med_insurance']
#            else:
#                saved_profile.med_insurance = saved_profile.med_insurance
#            if key == 'sex' is not None:
#                saved_profile.sex = update_profile['sex']
#            else:
#                saved_profile.sex = saved_profile.sex

        saved_profile.save()

        serializer = UserProfileSerializer(saved_profile)

        return Response({f"User {user.username} update profile successfully": serializer.data})
