# Generated by Django 4.0.3 on 2023-08-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_intro_photo_alter_product_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='intro',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
