# Generated by Django 4.1.3 on 2023-01-06 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0011_remove_post_images_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]
