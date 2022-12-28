# Generated by Django 4.1.2 on 2022-12-27 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_rename_active_comment_available_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deslike',
            field=models.ManyToManyField(blank=True, related_name='deslike_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]