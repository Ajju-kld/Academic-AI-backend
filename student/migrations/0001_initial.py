# Generated by Django 5.0.3 on 2024-03-18 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('semester', models.IntegerField()),
                ('scheme', models.CharField(max_length=20)),
                ('credits', models.IntegerField()),
                ('study_time', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('max_time', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('prequist', models.CharField(max_length=100)),
                ('focus_area', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]