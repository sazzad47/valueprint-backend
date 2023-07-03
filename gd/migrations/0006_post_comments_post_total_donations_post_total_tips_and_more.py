# Generated by Django 4.0.3 on 2023-06-27 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_biography'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gd', '0005_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='post_comments', through='gd.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='total_donations',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='post',
            name='total_tips',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gd.post'),
        ),
    ]
