# Generated by Django 2.2.7 on 2019-11-12 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BiceaterAPI', '0002_auto_20191111_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rating_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(default=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bike_hire_docking_station_id', models.CharField(default='0', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BiceaterAPI.User')),
            ],
        ),
    ]