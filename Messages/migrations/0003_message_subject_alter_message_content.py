# Generated by Django 4.1.3 on 2023-01-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0002_alter_message_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
