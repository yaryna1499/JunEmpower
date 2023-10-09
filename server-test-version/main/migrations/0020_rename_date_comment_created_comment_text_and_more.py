# Generated by Django 4.2.4 on 2023-10-09 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_project_title_gin_idx_project_description_gin_idx"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="date",
            new_name="created",
        ),
        migrations.AddField(
            model_name="comment",
            name="text",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="main.project",
            ),
        ),
    ]
