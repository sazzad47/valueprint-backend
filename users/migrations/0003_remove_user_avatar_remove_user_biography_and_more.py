# Generated by Django 4.0.3 on 2023-07-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='user',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expertise',
        ),
        migrations.RemoveField(
            model_name='user',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='user',
            name='place_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='user',
            name='social_links',
        ),
    ]