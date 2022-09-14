# Generated by Django 4.1 on 2022-09-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georga', '0013_rename_updated_at_ace_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolespecification',
            name='necessity',
            field=models.CharField(choices=[('MANDATORY', 'mandatory'), ('RECOMMENDED', 'recommended'), ('UNRECOMMENDED', 'unrecommended'), ('IMPOSSIBLE', 'impossible')], default='RECOMMENDED', max_length=13, verbose_name='necessity'),
        ),
    ]