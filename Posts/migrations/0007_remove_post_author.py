# Generated by Django 4.1.3 on 2022-12-27 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]