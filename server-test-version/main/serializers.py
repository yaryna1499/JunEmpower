from rest_framework import serializers
from .models import CustomUser, ProjectImage, Project, Technology


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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'project', 'image', 'is_main')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'title')


class ProjectSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technology', 'author', 'images']


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology']