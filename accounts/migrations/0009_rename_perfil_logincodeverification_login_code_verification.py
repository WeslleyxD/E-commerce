# Generated by Django 4.1.2 on 2022-11-04 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_logincodeverification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logincodeverification',
            old_name='perfil',
            new_name='login_code_verification',
        ),
    ]