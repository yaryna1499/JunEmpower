from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.indexes import GinIndex
from cloudinary.models import CloudinaryField

class Specialization(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Technology(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class CustomUser(AbstractUser):

    def profile_picture_file_name(self):
        return f"avatar_of_user_{self.username}"

    email = models.EmailField(unique=True)
    profile_picture = CloudinaryField("profile_picture", folder='users/profile', overwrite=True,
  transformation=[
  {'aspect_ratio': "1.0", 'width': 150, 'crop': "fill"},
  {'radius': "max"},
  {'fetch_format': "auto"},
  {"quality": 80},
  ], use_filename=True, public_id=profile_picture_file_name)
    
    specialization = models.ManyToManyField(Specialization, blank=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    repo = models.URLField(max_length=200, blank=True, null=True)
    telegram = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    technology = models.ManyToManyField(Technology, blank=True)
    tags = models.TextField(max_length=500, blank=True, null=True)
    link_hub = models.URLField(blank=True, null=True)
    link_deploy = models.URLField(blank=True, null=True)
    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("in_development", "In Development"),
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="in_development"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            GinIndex(fields=['title'], name='title_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['description'], name='description_gin_idx', opclasses=['gin_trgm_ops']),
        ]

    @property
    def main_image(self):
        return (
            ProjectImage.objects.filter(Q(project_id=self.id) & Q(is_main=True))
            .first()
            .image
        )

    @property
    def all_images(self):
        return (
            ProjectImage.objects.filter(project_id=self.id)
            .values_list("image", flat=True)
            .order_by("-is_main")
        )

    def __str__(self):
        return f"Project {self.title}, id: {self.id}"


class ProjectImage(models.Model):

    def project_image_file_name(self):
        return f"image_of_project_{self.project}_with_id_{self.id}"

    def project_image_folder_name(self):
        return f"projects/project_{self.project}"


    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = CloudinaryField("project_image", folder=project_image_folder_name, overwrite=True,
  transformation=[
  {"width": 400, "height": 300, "crop": "pad"},
  {'fetch_format': "auto"},
  {"quality": 80},
  ], use_filename=True, public_id=project_image_file_name)
    
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image id: {self.id} for project id: {self.project}"


class Like(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="likes")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "author",
            "project",
        )  # це потрібно щоб один юзер міг поставити під конкретним постом тільки один лайк.


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.project.title}"
