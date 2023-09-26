from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import ProjectImage

User = get_user_model()


@receiver(pre_save, sender=ProjectImage)
def update_main_image(sender, instance, **kwargs):
    if instance.is_main:
        sender.objects.filter(project=instance.project, is_main=True).exclude(
            id=instance.id
        ).update(is_main=False)


@receiver(post_save, sender=ProjectImage)
def ensure_main_image_exists(sender, instance, created, **kwargs):
    if (
        created
        and not sender.objects.filter(project=instance.project, is_main=True).exists()
    ):
        instance.is_main = True
        instance.save()
