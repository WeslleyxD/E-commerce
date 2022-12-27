# Generated by Django 4.1.2 on 2022-12-27 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='products.comment'),
        ),
    ]
