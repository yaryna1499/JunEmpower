from django.contrib import admin
from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]


admin.site.register(CustomUser)
admin.site.register(Project, PostAdmin)