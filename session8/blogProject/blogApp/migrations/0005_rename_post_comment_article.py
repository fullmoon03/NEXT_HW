# Generated by Django 4.1.7 on 2023-04-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='article',
        ),
    ]
