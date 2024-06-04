from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users_app.models import User
from users_app.serializers.register import RegisterModelSerializer


class RegisterCreateAPiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
    permission_classes = [AllowAny, ]