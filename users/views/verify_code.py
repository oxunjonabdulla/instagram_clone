from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import NEW, CONFIRMED


class VerifyApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user = request.user
        code = request.data.get("code")

        self.check_verify(user=user,
                          code=code)
        return Response(
            {
                "success": True,
                "user_status": user.auth_status,
                "access_token": user.token()['access_token'],
                "refresh_token": user.token()['refresh_token']
            }
        )

    @staticmethod
    def check_verify(user, code):
        verifies = user.user_confirmations.filter(expiration_time__gte=timezone.now(),
                                                  code=code, is_confirmed=False)
        print(verifies)
        if not verifies.exists():
            data = {
                "success": False,
                "message": "Invalid code "
            }
            raise ValidationError(data)

        else:
            verifies.update(is_confirmed=True)
            if user.auth_status == NEW:
                user.auth_status = CONFIRMED
                user.save()
            data = {
                "success": True,
                "message": "User successfully confirmed"
            }
            return data
