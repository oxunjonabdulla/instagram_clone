from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

from users.serializers.login_refresh import LoginRefreshSerializer


class LoginRefreshView(TokenRefreshView):
    serializer_class = LoginRefreshSerializer
