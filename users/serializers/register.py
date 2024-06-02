from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shared.utils import send_email, check_email_or_phone_number
from users.models import User, VIA_EMAIL, VIA_PHONE


class RegisterModelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    # email_or_phone_number = serializers.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(RegisterModelSerializer, self).__init__(*args, **kwargs)
        self.fields['email_or_phone_number'] = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "auth_type",
            "auth_status"
        )
        extra_kwargs = {
            "auth_type": {
                "read_only": True,
                "required": False
            },
            "auth_status": {
                "read_only": True,
                "required": False
            }
        }

    def create(self, validated_data):
        user = super(RegisterModelSerializer, self).create(validated_data)
        if user.auth_type == VIA_EMAIL:
            code = user.create_verify_code(verify_type=VIA_EMAIL)
            send_email(email=user.email, code=code)
        elif user.auth_type == VIA_PHONE:
            code = user.create_verify_code(verify_type=VIA_PHONE)
            print(f"code: {code}")

            # send_phone_numer_code(phone_number=VIA_PHONE,
            #                       code=code)
            send_email(VIA_PHONE, code=code)

        user.save()
        return user

    def validate(self, data):
        super(RegisterModelSerializer, self).validate(data)
        data = self.auth_validate(data)
        return data

    @staticmethod
    def auth_validate(data):
        user_input = str(data.get("email_or_phone_number", ""))
        input_type = check_email_or_phone_number(email_or_phone_number=user_input)
        if User.objects.filter(email=user_input).exists() or User.objects.filter(phone_number=user_input).exists():
            data = {
                "success": False,
                "message": "User already exists"
            }
            raise ValidationError(data)
        else:
            if input_type == "email":
                data = {
                    "email": user_input,
                    "auth_type": VIA_EMAIL,
                }
            elif input_type == "phone_number":
                data = {
                    "phone_number": user_input,
                    "auth_type": VIA_PHONE,
                }
            else:
                data = {
                    "success": False,
                    "message": "You entered an invalid email or phone number"
                }
                raise ValidationError(data)

            return data

    def to_representation(self, instance):
        data = super(RegisterModelSerializer, self).to_representation(instance)
        data.update(instance.token())
        return data
