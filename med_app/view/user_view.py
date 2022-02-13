from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from med_app.models import User
from med_app.serializers import UserSerializer, UserListSerializer


class UserAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        #        try:
        #            id = request.query_params['id']
        #            if id is not None:
        #                users = User.objects.get(id=id)
        #                serializer = UserSerializer(users)
        #
        #        except:
        #            users = User.objects.all()
        #            serializer = UserListSerializer(users)
        #
        #        return Response(serializer.data)

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user).data
        return Response(serializer)

    def put(self, request):
        user_id = request.user.id
        saved_user = get_object_or_404(User.objects.all(), id=user_id)

        user = request.user
        updating_user = request.data
        for i in updating_user:
            if i == 'username' is not None:
                saved_user.username = updating_user['username']
            else:
                saved_user.username = user.username
            if i == 'email' is not None:
                saved_user.email = updating_user['email']
            else:
                saved_user.email = user.email
            if i == 'password' is not None:
                saved_user.password = updating_user['password']
            else:
                saved_user.password = user.password
            if i == 'phone_number' is not None:
                saved_user.phone_number = updating_user['phone_number']
            else:
                saved_user.phone_number = user.phone_number

        saved_user.save()

        serializer = UserSerializer(saved_user)
        return Response({f"User with Id:{saved_user.id} updated successfully": serializer.data})

    def delete(self, request):
        user_id = request.user.id
        user = get_object_or_404(User.objects.all(), id=user_id)

        user.delete()

        return Response(f"User with Id:{id} deleted successfully")
