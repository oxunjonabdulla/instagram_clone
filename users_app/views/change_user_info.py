from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.serializers.change_user_info import ChangeUserInformationSerializer


class ChangeUserInformationUpdateAPIView(UpdateAPIView):
    serializer_class = ChangeUserInformationSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['put', "patch"]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        super(ChangeUserInformationUpdateAPIView, self).update(request, *args, **kwargs)
        data = {
            "success": True,
            "message": "User successfully updated",
            "auth_status": self.request.user.auth_status
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        data = {
            "success": True,
            "message": "User successfully updated",
            "auth_status": self.request.user.auth_status
        }
        return Response(data=data, status=status.HTTP_200_OK)
