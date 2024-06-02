from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.change_user_image import ChangeUserImageSerializer


class ChangeUserImageView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        serializer = ChangeUserImageSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.update(
                user, validated_data=serializer.validated_data
            )
            return Response(
                data={
                    "success": True,
                    "message": 'Successfully user image changed'
                },
                status=status.HTTP_200_OK
            )
        return Response(
                data={
                    serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
