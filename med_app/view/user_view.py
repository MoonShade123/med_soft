from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from med_app.models import User
from med_app.serializers import UserSerializer, UserListSerializer


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    user_serializer = UserSerializer

    def get(self, request):
        try:
            id = request.query_params['id']
            if id is not None:
                users = User.objects.get(id=id)
                serializer = UserSerializer(users)

        except:
            users = User.objects.all()
            serializer = UserListSerializer(users)

        return Response(serializer.data)

    def put(self, request):
        id = request.query_params['id']
        saved_user = get_object_or_404(User.objects.all(), id=id)

        user = request.data

        saved_user.username = user['username']
        saved_user.password = user['password']
        saved_user.phone_number = user['phone_number']

        saved_user.save()

        serializer = UserSerializer(saved_user)
        return Response({f"User with Id:{saved_user.id} updated successfully": serializer.data})

    def delete(self, request):
        id = request.query_params['id']
        user = get_object_or_404(User.objects.all(), id=id)

        user.delete()

        return Response(f"User with Id:{id} deleted successfully")
