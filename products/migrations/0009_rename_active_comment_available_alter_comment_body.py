# Generated by Django 4.1.2 on 2022-12-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_product_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='available',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='', max_length=600),
        ),
    ]
