# Generated by Django 4.2.4 on 2023-09-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_specialization_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialization",
            name="slug",
            field=models.CharField(default="slug", max_length=100, unique=True),
        ),
    ]