# Generated by Django 4.0.3 on 2023-07-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ip',
        ),
        migrations.AddField(
            model_name='product',
            name='dp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]