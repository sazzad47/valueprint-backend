# Generated by Django 4.0.3 on 2023-07-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_option_price_schema_subvariant_variant_yourmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='subvariant',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='layout',
        ),
    ]
