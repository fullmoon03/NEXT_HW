# Generated by Django 4.2 on 2023-04-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_list_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
