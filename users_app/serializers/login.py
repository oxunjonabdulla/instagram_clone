from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from shared_app.utils import check_user_type
from users_app.models import User, CONFIRMED, NEW, IMAGE_STEP, DONE


class LoginSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields['user_input'] = serializers.CharField(required=True)
        self.fields['username'] = serializers.CharField(required=False, read_only=True)

    def auth_validate(self, data):
        user_input = data.get("user_input")
        password = data.get("password")
        if check_user_type(user_input=user_input) == "username":
            username = user_input
        elif check_user_type(user_input=user_input) == "email":
            user = User.objects.filter(email=user_input).first()
            if not user:
                data = {
                    "success": False,
                    "message": "User not found"
                }
                raise ValidationError(data)
            username = user.username
        elif check_user_type(user_input=user_input) == "phone_number":
            user = User.objects.filter(phone_number=user_input).first()
            if not user:
                data = {
                    "success": False,
                    "message": "User not found"
                }
                raise ValidationError(data)
            username = user.username
        else:
            data = {
                "success": False,
                "message": "Email, username or phone_numer is not correct"
            }
            raise ValidationError(data)

        authentication_kwargs = {
            self.username_field: username,
            "password": password
        }
        current_user = User.objects.filter(username__iexact=username).first()
        if current_user is not None and current_user.auth_status in [NEW, CONFIRMED]:
            data = {
                "success": False,
                "message": "Siz hali to'liq ro'yxatdan o'tmagansiz"
            }
            raise ValidationError(data)
        else:
            user = authenticate(**authentication_kwargs)
            if user is not None:
                self.user = user
            else:
                data = {
                    "success": False,
                    "messages": "Sorry login or password you entered is "
                }
                raise ValidationError(data)

    def validate(self, data):
        self.auth_validate(data=data)
        print(f"User stat")
        if self.user.auth_status not in [DONE, IMAGE_STEP]:
            data = {
                "success": False,
                "messages": "Siz login qila olmaysiz"
            }
            raise ValidationError(data)
        else:
            data = self.user.token()
            data['auth_status'] = self.user.auth_status
            return data
