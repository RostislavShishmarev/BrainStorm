# Generated by Django 3.2.16 on 2023-04-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_description'),
        ('projects', '0003_project_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='tags.Tag', verbose_name='теги'),
        ),
    ]
