# Generated by Django 3.2.16 on 2023-04-10 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(help_text='Какому проекту принадлежит комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='commants', to='projects.project', verbose_name='проект'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
