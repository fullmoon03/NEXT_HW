# Generated by Django 4.2 on 2023-04-08 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_list_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='deadline',
            new_name='end_date',
        ),
    ]
