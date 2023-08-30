from django.contrib.auth.models import AbstractUser
from django.db import models


class Specialization(models.Model):
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.specialization


class Technology(models.Model):
    technology = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.technology


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    profile_picture = models.ImageField(
        upload_to="uploads/profile/", blank=True, null=True
    )
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.username

    # USERNAME_FIELD = 'Email or Username'
    # REQUIRED_FIELDS = ['Password']


    # @classmethod                                   для чого це? мабудь були проблеми з полем email того шо воно вже є..
    # def user_exists(cls, email):
    #     return cls.objects.filter(email=email).exists()


class Project(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.TextField(max_length=500, blank=True, null=True)

    @property
    def main_image(self):
        return ProjectImage.objects.filter(Q(project_id=self.id) & Q(is_main=True)).first().image

    @property
    def all_images(self):
        return ProjectImage.objects.filter(project_id=self.id).values_list('image', flat=True).order_by('-is_main')

    def __str__(self):
        return f"Project {self.title}, id: {self.id}"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="uploads/img/project/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image id: {self.id} for post id: {self.post}"


class Like(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author_id', 'project')  # це потрібно щоб один юзер міг поставити під конкретним постом тільки один лайк.


class Comment(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
