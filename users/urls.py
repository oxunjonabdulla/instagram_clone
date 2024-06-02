from django.urls import path

from users.views.change_user_image import ChangeUserImageView
from users.views.change_user_info import ChangeUserInformationUpdateAPIView
from users.views.forgot_password import ForgotPasswordAPIView
from users.views.login import LoginView
from users.views.login_refresh import LoginRefreshView
from users.views.logout import LogoutAPIView
from users.views.register import RegisterCreateAPiView
from users.views.repeat_get_verify_code import GetVerifyCodeAPiView
from users.views.reset_password import ResetPasswordUpdateAPIView
from users.views.verify_code import VerifyApiView

urlpatterns = [
    path('register/', RegisterCreateAPiView.as_view(), name="register"),

    path("verify/", VerifyApiView.as_view(), name="verify"),
    path("repeat_code/", GetVerifyCodeAPiView.as_view(), name="repeat_code"),

    path("login/", LoginView.as_view(), name='login'),
    path("login_refresh/", LoginRefreshView.as_view(), name="login_refresh"),

    path("change_user_info/", ChangeUserInformationUpdateAPIView.as_view(), name="change_user_info"),
    path("change_user_image/", ChangeUserImageView.as_view(), name="change_user_image"),

    path("logout/", LogoutAPIView.as_view(),name="logout"),

    path('forgot_password/', ForgotPasswordAPIView.as_view(), name="forgot_password"),
    path("reset_password/", ResetPasswordUpdateAPIView.as_view(), name="reset_password")

]
