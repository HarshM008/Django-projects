# Generated by Django 4.1.5 on 2023-01-16 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='description',
            new_name='desc',
        ),
    ]
