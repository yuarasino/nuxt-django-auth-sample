from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class HelloView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            "hello": f"Hello {user.username}!"
        })
