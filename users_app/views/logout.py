from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from users_app.serializers.logout import LogoutSerializer


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token =  self.request.data['refresh_token']
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            data = {
                "success":True,
                "message":"Successfully logged out"
            }
            return Response(data=data,
                            status=status.HTTP_200_OK)
        except TokenError:
            data = {
                "saccess": False,
                "message": "Token not found"
            }
            return Response(data=data,
                            status=status.HTTP_400_BAD_REQUEST)

