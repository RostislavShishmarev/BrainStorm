# Generated by Django 3.2.16 on 2023-04-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration', '0004_auto_20230417_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborationrequest',
            name='answer',
            field=models.TextField(blank=True, verbose_name='ответ автора проекта'),
        ),
        migrations.AlterField(
            model_name='collaborationrequest',
            name='contact',
            field=models.TextField(blank=True, max_length=150, verbose_name='информация о контактах'),
        ),
    ]
