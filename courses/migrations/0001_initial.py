# Generated by Django 5.0.3 on 2024-05-11 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('bacth_year', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('scheme', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('semester', models.CharField(default='', max_length=100)),
                ('series_one_date', models.DateField()),
                ('series_two_date', models.DateField()),
                ('end_semester_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('MECH', 'Mechanical Engineering'), ('IT', 'Information Technology'), ('EC', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering')], max_length=100)),
                ('subject_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('no_of_modules', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('scheme', models.CharField(max_length=20)),
                ('subject_name', models.CharField(max_length=100)),
                ('credits', models.IntegerField()),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('max_time', models.IntegerField(blank=True, null=True)),
                ('module', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('focus_area', models.BooleanField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject')),
            ],
        ),
    ]
