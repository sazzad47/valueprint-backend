# Generated by Django 4.0.3 on 2023-07-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_order_details_alter_order_shipping_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
