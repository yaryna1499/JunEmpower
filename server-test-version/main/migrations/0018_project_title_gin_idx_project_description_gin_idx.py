# Generated by Django 4.2.4 on 2023-10-01 16:25

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_alter_project_title"),
    ]

    # operations = [
    #     TrigramExtension(),
    #     migrations.RunSQL(
    #         "CREATE OPERATOR CLASS gin_trgm_ops "
    #         "DEFAULT FOR TYPE text USING gin AS "
    #         "OPERATOR 1 <(text,text), "
    #         "OPERATOR 2 =(text,text), "
    #         "OPERATOR 3 >(text,text), "
    #         "FUNCTION 1 text_cmp(text,text), "
    #         "FUNCTION 2 text_sortsupport(internal);"
    #     ),
    #     migrations.RunSQL(
    #         "CREATE INDEX title_gin_idx ON main_project USING gin (title gin_trgm_ops);"
    #     ),
    #     migrations.RunSQL(
    #         "CREATE INDEX description_gin_idx ON main_project USING gin (description gin_trgm_ops);"
    #     ),
    # ]