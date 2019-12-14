# Generated by Django 2.2.7 on 2019-12-02 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0029_auto_20191126_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('birth_date', models.DateField(max_length=10)),
                ('address', models.CharField(choices=[('Banaadir', 'Banaadir'), ('Jubbada Dhexe', 'Jubbada Dhexe'), ('Jubbada Hoose', 'Jubbada Hoose'), ('Mudug', 'Mudug'), ('Hiiran', 'Hiiran'), ('Awdal', 'Awdal'), ('Bakool', 'Bakool'), ('Bari', 'Bari'), ('Baay', 'Baay'), ('Galgaduud', 'Galgaduud'), ('Gedo', 'Gedo'), ('Nugaal', 'Nugaal'), ('Sanaag', 'Sanaag'), ('Shabeellaha Hoose', 'Shabeellaha Hoose'), ('Shabeellaha Dhexe', 'Shabeellaha Dhee'), ('Sool', 'Sool'), ('Togdheer', 'Togdheer'), ('Woqooyi Galbeed', 'Woqooyi Galbeed')], default='Banaadir', max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='value',
        ),
        migrations.AddField(
            model_name='ticket',
            name='has_cancelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ticket',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_type',
            field=models.CharField(choices=[('Nurse', 'Nurse'), ('Other', 'Other')], default='Nurse', max_length=5),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Doctor'),
        ),
    ]
