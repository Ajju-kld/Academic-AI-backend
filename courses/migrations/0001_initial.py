# Generated by Django 5.0.3 on 2024-03-21 08:21

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
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('exam_type', models.CharField(max_length=100)),
                ('exam_credits', models.IntegerField(blank=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.batch')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject')),
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
