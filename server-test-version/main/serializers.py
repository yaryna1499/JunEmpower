from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    CustomUser,
    ProjectImage,
    Project,
    Technology,
    Specialization,
    Like,
    Comment,
)


from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token


class SpecializationSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Specialization
        fields = ("id", "title", "slug")


class CustomUserSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True, many=True)

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
            "specialization",
            "about",
            "country",
            "linkedin",
            "repo",
            "telegram",
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    # specialization = SpecializationSerializer(read_only=True, many=True)
    specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all(), many=True)
    password = serializers.CharField(write_only=True)

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
            "specialization",
            "about",
            "country",
            "linkedin",
            "repo",
            "telegram",
        ]
        read_only_fields = ['id', ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)  # Захешувати пароль
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance



# _________project____________________#


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ("id", "project", "image", "is_main")


class TechnologySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Technology
        fields = ("id", "title", "slug")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    author = CustomUserSerializer(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "created",
            "technology",
            "author",
            "images",
            "likes",
            "status",
            "link_hub",
            "link_deploy",
            "comments",
        ]


class ProjectCreateSerializer(serializers.ModelSerializer):
    technology = serializers.PrimaryKeyRelatedField(
        queryset=Technology.objects.all(), many=True
    )
    # id = serializers.ReadOnlyField()

    class Meta:
        model = Project

        fields = ["id", "title", "description", "technology", "link_hub", "link_deploy", "status"]

    def create(self, validated_data):
        technology_data = validated_data.pop("technology", [])
        project = Project(**validated_data)
        project.save()
        for technology in technology_data:
            if technology:
                project.technology.add(technology)

        return project

    def update(self, instance, validated_data):
        technology_data = validated_data.pop("technology", [])
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if technology_data:
            instance.technology.clear()
            for technology in technology_data:
                instance.technology.add(technology)
        instance.save()
        return instance
