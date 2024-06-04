from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.models import User
from users_app.serializers.reset_password import ResetPasswordSerializer


class ResetPasswordUpdateAPIView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['put', "patch"]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super(ResetPasswordUpdateAPIView, self).update(request, *args, **kwargs)
        try:
            user = User.objects.filter(id=response.data.get("id")).first()
        except ObjectDoesNotExist as e:
            raise NotFound(detail="User Not found")
        return Response(
            {
                "success": True,
                "message": "Parolingiz muvaffaqiyatli ravishda o'zgartirildi",
                "access_token": user.token()['access_token'],
                "refresh_token": user.token()['refresh_token'],
            }
        )
