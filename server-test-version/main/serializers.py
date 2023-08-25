from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "profile_picture",
            "is_active",
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')  # Отримати пароль з даних

        user = CustomUser(**validated_data)
        user.set_password(password)  # Захешувати пароль
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



    