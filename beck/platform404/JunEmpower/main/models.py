from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):
    name_skill = models.CharField(max_length=50)

    def __str__(self):
        return self.name_skill


class CustomUser(AbstractUser):
    CHOICES = (
        ('developer', 'Developer'),
        ('company', 'Company')
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    profile_picture = models.ImageField(upload_to="uploads/profile/", blank=True, null=True)
    profile_type = models.CharField(max_length=20, choices=CHOICES)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    biography = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username


