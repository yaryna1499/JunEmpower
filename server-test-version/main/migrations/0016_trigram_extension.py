from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_customuser_about_customuser_country_and_more"),
    ]

    operations = [
        TrigramExtension(),
    ]