# Generated by Django 4.0.3 on 2023-07-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='design_services',
            field=models.JSONField(blank=True, null=True),
        ),
    ]