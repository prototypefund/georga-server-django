# Generated by Django 4.1 on 2022-09-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0014_alter_rolespecification_necessity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='operation',
        ),
    ]
