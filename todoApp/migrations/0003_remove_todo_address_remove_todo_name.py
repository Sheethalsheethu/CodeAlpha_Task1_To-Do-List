# Generated by Django 5.0.6 on 2024-05-13 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_remove_todo_fee_todo_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
    ]
