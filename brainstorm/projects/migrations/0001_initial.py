# Generated by Django 3.2.16 on 2023-04-05 19:43

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Назовите проект', max_length=150, verbose_name='название')),
                ('description', models.TextField(help_text='Введите описание проекта', verbose_name='описание')),
                ('published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('in_archive', models.BooleanField(default=False, verbose_name='в архиве')),
                ('status', models.CharField(choices=[('development', 'В разработке'), ('ready', 'Готов')], default='development', max_length=14, verbose_name='статус проетка')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('author', models.ForeignKey(help_text='Кто автор', on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('collaborators', models.ManyToManyField(blank=True, null=True, related_name='colleagues', to=settings.AUTH_USER_MODEL, verbose_name='коллабораторы')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=core.models.directory_path, verbose_name='фотка')),
                ('project', models.OneToOneField(help_text='Какому проекту принадлежит превью', on_delete=django.db.models.deletion.CASCADE, related_name='preview', to='projects.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'превью',
                'verbose_name_plural': 'превьюшки',
            },
        ),
        migrations.CreateModel(
            name='ImagesGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=core.models.directory_path, verbose_name='фотка')),
                ('project', models.ForeignKey(help_text='Какому проекту принадлежит картинка', on_delete=django.db.models.deletion.CASCADE, related_name='images_gallery', to='projects.project', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'картинки',
            },
        ),
    ]
