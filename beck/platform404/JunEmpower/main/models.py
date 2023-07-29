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


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    demonstration = models.URLField(blank=True, null=True)
    github_repository_url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.project_name}"


class ProjectLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='likes')
    like_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} liked {self.project.project_name}"

