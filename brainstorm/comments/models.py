import django.contrib.auth.models
import django.db.models
import projects.models

import users.models


class Comment(django.db.models.Model):
    project = django.db.models.ForeignKey(
        projects.models.Project,
        verbose_name='проект',
        related_name='comment',
        on_delete=django.db.models.CASCADE,
        help_text='Какому проекту принадлежит комментарий',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name='пользователь',
        related_name='comment',
    )
    text = django.db.models.TextField(
        'комментарий',
        help_text='Оставить комментарий',
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text[:15]
