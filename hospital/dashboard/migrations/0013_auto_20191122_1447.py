# Generated by Django 2.2 on 2019-11-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20191122_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='updated_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
