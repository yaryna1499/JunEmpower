from django.contrib import admin
from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, PostAdmin)
admin.site.register(Specialization)
admin.site.register(Technology)
admin.site.register(Like)
admin.site.register(Comment)
