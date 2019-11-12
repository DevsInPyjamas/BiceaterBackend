# Generated by Django 2.2.7 on 2019-11-08 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, max_length=50)),
                ('DoB', models.DateField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('hobbies', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stop_id', models.IntegerField()),
                ('answers_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BiceaterAPI.Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BiceaterAPI.User')),
            ],
        ),
    ]