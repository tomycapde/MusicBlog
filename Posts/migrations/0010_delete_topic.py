# Generated by Django 4.1.3 on 2023-01-04 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0009_alter_post_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
    ]