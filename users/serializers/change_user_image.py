from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from users.models import IMAGE_STEP


class ChangeUserImageSerializer(serializers.Serializer):
    image = serializers.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=[
            "jpg", "jpeg", "png", "heic"
        ])]
    )

    def update(self, instance, validated_data):
        image = validated_data.get("image")
        if image:
            instance.image = image
            instance.auth_status = IMAGE_STEP
            instance.save()
        return instance