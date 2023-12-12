import logging

import cloudinary
import cloudinary.uploader
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from .models import CustomUser, ProjectImage

User = get_user_model()


@receiver(pre_save, sender=ProjectImage)
def update_main_image(sender, instance, **kwargs):
    if instance.is_main:
        sender.objects.filter(project=instance.project, is_main=True).exclude(id=instance.id).update(is_main=False)


@receiver(post_save, sender=ProjectImage)
def ensure_main_image_exists(sender, instance, created, **kwargs):
    if created and not sender.objects.filter(project=instance.project, is_main=True).exists():
        instance.is_main = True
        instance.save()


@receiver(pre_save, sender=User)
def delete_image_from_cloudinary(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        old_instance = None

    if old_instance:
        old_field_value = old_instance.profile_picture
        if old_field_value:
            if instance.profile_picture is None:
                cloudinary.uploader.destroy(old_field_value.public_id, invalidate=True)
