from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shared_app.utils import check_email_or_phone_number, send_email
from users_app.models import VIA_EMAIL, VIA_PHONE
from users_app.serializers.forgot_password import ForgotPasswordSerializer


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email_or_phone_number = serializer.validated_data.get("email_or_phone_number")
        print(f"Ema{ email_or_phone_number}")
        user = serializer.validated_data.get("user")
        print(f"User : {user}")
        if check_email_or_phone_number(email_or_phone_number) == "email":
            code = user.create_verify_code(VIA_EMAIL)
            send_email(email_or_phone_number, code=code)

        elif check_email_or_phone_number(email_or_phone_number) == "phone_number":
            code = user.create_verify_code(VIA_PHONE)
            # send_phone_numer_code(user.phone_number, code)
            send_email(email_or_phone_number, code=code)

        return Response(
            data={
                "success": True,
                "message": f"Sizning {email_or_phone_number} ga tasdiqlash kodi yuborildi !",
                "access_token": user.token()['access_token'],
                "refresh_token": user.token()["refresh_token"],
                "auth_status": user.auth_status
            },
            status=status.HTTP_200_OK
        )
