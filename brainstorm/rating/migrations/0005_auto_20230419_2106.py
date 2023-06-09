# Generated by Django 3.2.16 on 2023-04-19 18:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0013_auto_20230419_2106'),
        ('rating', '0004_alter_projectrating_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectrating',
            options={'verbose_name': 'rating', 'verbose_name_plural': 'ratings'},
        ),
        migrations.AlterField(
            model_name='projectrating',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_project', to='projects.project', verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='projectrating',
            name='score',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='projectrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_project_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.DeleteModel(
            name='CommentRating',
        ),
    ]
