from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser, ProjectImage, Project, Technology, Specialization


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('id', 'title', 'slug')


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
            "specialization"
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True, many=True)
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
            "specialization"

        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        specialization_data = validated_data.pop('specialization', [])

        user = CustomUser(**validated_data)
        user.set_password(password)  # Захешувати пароль

        for specialization in specialization_data:    # спробувати тут примінити setatr() замість for
            if specialization:
                user.specialization.add(specialization)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        specialization_data = validated_data.pop('specialization', [])
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        if specialization_data:
            instance.specialization.clear()
            for specialization in specialization_data:
                instance.specialization.add(specialization)

        instance.save()
        return instance


#_________project____________________#



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'project', 'image', 'is_main')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'title', 'slug')


class ProjectSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technology', 'author', 'images']


class ProjectCreateSerializer(serializers.ModelSerializer):
    technology = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'technology']

    def create(self, validated_data):
        technology_data = validated_data.pop('technology', [])
        project = Project(**validated_data)
        for technology in technology_data:
            if technology:
                project.technology.add(technology)
        project.save()
        return project

    def update(self, instance, validated_data):
        technology_data = validated_data.pop('technology', [])
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if technology_data:
            instance.technology.clear()
            for technology in technology_data:
                instance.technology.add(technology)
        instance.save()
        return instance

