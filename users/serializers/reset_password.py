from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class ResetPasswordSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(min_length=8,
                                     write_only=True, required=True)
    confirm_password = serializers.CharField(min_length=8,
                                     write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "confirm_password"
        )

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']
        if password != confirm_password:
            raise ValidationError(
                {
                    'success': False,
                    "message": "password and confirm_password do not match"
                }
            )
        if password:
            validate_password(password)
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance