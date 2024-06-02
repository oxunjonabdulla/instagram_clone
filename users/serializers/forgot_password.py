from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound

from users.models import User


class ForgotPasswordSerializer(serializers.Serializer):
    email_or_phone_number = serializers.CharField(required=True,
                                                  write_only=True)

    def validate(self, data):
        email_or_phone_number = data.get("email_or_phone_number", None)
        if email_or_phone_number is None:
            raise ValidationError({
                "success": False,
                "message": "Email or phone number is required"
            })

        user = User.objects.filter(
            Q(email=email_or_phone_number)|
            Q(phone_number=email_or_phone_number)
        )

        if not user.exists():
            raise NotFound(
                {
                    "success": False,
                    "message": "User not found"
                }
            )
        data['user'] = user.first()
        return data
