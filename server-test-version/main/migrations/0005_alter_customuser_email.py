# Generated by Django 4.2.4 on 2023-08-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_project_tags_projectimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
