from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User, CONFIRMED, DONE


class ChangeUserInformationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "password", "confirm_password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            data = {
                "success": False,
                "message": "Password and confirm password do not match"
            }
            raise ValidationError(data)
        validate_password(password=password)
        return data

    def validate_username(self, username):
        if len(username) < 5 or len(username) > 30:
            raise ValidationError({
                'success': False,
                'message': 'Username must be between 5 and 30 characters'
            })
        if username.isdigit():
            raise ValidationError({
                'success': False,
                'message': 'Username must contain letters'
            })
        return username

    def validate_first_name(self, first_name):
        if len(first_name) < 5 or len(first_name) > 30:
            raise ValidationError({
                'success': False,
                'message': 'first_name must be between 5 and 30 characters'
            })
        if first_name.isdigit():
            raise ValidationError({
                'success': False,
                'message': 'first_name must contain letters'
            })
        return first_name

    def validate_last_name(self, last_name):
        if len(last_name) < 5 or len(last_name) > 30:
            raise ValidationError({
                'success': False,
                'message': 'last_name must be between 5 and 30 characters'
            })
        if last_name.isdigit():
            raise ValidationError({
                'success': False,
                'message': 'last_name must contain letters'
            })
        return last_name

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)
        if instance.auth_status == CONFIRMED:
            instance.auth_status = DONE
        instance.save()
        return instance
