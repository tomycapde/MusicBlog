# Generated by Django 4.1.3 on 2022-12-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_avatar_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
