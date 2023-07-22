# Generated by Django 4.0.3 on 2023-07-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_order_additional_file_remove_order_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
