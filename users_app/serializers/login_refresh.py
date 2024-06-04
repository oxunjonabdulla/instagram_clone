from django.contrib.auth.models import update_last_login
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken

from users_app.models import User


class LoginRefreshSerializer(TokenRefreshSerializer):

    def validate(self, data):
        data = super().validate(data)
        access_token_instance = AccessToken(data.get("access"))
        user_id = access_token_instance['user_id']
        user = get_object_or_404(User, id=user_id)
        update_last_login(None, user)
        return data
