# Generated by Django 4.2.13 on 2024-06-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_trainer', models.CharField(max_length=100)),
                ('course_objective', models.CharField(max_length=255)),
                ('course_duration', models.DurationField()),
                ('course_description', models.TextField()),
                ('pass_mark', models.IntegerField()),
                ('course_title', models.CharField(max_length=100)),
                ('course_teacher', models.CharField(max_length=100)),
                ('course_resources', models.CharField(max_length=255)),
                ('teaching_assistant', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
