# Generated by Django 2.2.7 on 2019-12-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0051_auto_20191210_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labrequest',
            name='examined',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labrequest',
            name='paid',
            field=models.IntegerField(default=0),
        ),
    ]
