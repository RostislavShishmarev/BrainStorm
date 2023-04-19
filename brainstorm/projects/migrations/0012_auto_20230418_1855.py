# Generated by Django 3.2.16 on 2023-04-18 18:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_merge_20230418_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=ckeditor.fields.RichTextField(verbose_name='краткое описание'),
        ),
    ]
