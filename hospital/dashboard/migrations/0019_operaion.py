# Generated by Django 2.2.7 on 2019-11-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_operation_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operaion', models.CharField(max_length=50, unique=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Operation_Group')),
            ],
        ),
    ]
