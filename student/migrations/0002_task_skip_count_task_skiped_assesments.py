# Generated by Django 5.0.3 on 2024-05-13 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_exam_assignement_2_date_exam_assignment_1_date_and_more'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='skip_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='skiped',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Assesments',
            fields=[
                ('student', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('series_1', models.IntegerField(blank=True, null=True)),
                ('series_2', models.IntegerField(blank=True, null=True)),
                ('assignement_1', models.IntegerField(blank=True, null=True)),
                ('assignement_2', models.IntegerField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject')),
            ],
        ),
    ]
