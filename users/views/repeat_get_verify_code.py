from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shared.utils import send_email
from users.models import VIA_EMAIL, VIA_PHONE


class GetVerifyCodeAPiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.check_verification(user=user)
        if user.auth_type == VIA_EMAIL:
            code = user.create_verify_code(VIA_EMAIL)
            send_email(email=user.email,
                       code=code)
        elif user.auth_type == VIA_PHONE:
            code = user.create_verify_code(VIA_PHONE)

            # send_phone_numer_code(phone_number=user.phone_number,code=code)
            send_email(email=user.phone_number,
                       code=code)

        else:
            data = {
                "success": False,
                "message": "Phone number or email is not correct"
            }
            raise ValidationError(data)
        return Response(
            data={
                "success": True,
                "message": "Qaytadan kod yuborildi"
            }
        )

    @staticmethod
    def check_verification(user):
        verifies = user.user_confirmations.filter(expiration_time__gte=timezone.now(),
                                                  is_confirmed=False)
        if verifies.exists():
            data = {
                "success": False,
                "message": "Tasdiqlash kodi muddati tugagani yo'q"
            }
            raise ValidationError(data)
