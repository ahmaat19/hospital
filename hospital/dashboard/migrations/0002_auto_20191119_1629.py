# Generated by Django 2.2.7 on 2019-11-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='distict',
            new_name='district',
        ),
    ]
