# Generated by Django 2.2.1 on 2019-09-26 09:23

import datetime
from django.conf import settings
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100, verbose_name='Contact Number')),
                ('account_type', models.CharField(choices=[('', 'Select Account Type'), ('1', 'Student'), ('2', "Teacher's"), ('3', 'Corporate')], default=0, max_length=10)),
                ('email_id', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_super', models.CharField(default='user', max_length=20)),
                ('view_password', models.CharField(default='', max_length=150)),
            ],
            options={
                'db_table': 'superadmin',
            },
        ),
        migrations.CreateModel(
            name='SubjectManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_status', models.CharField(default='Active', max_length=20)),
                ('subject_created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('subject_created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subject_management',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=100)),
                ('question_status', models.CharField(default='Active', max_length=20)),
                ('question_created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('question_created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'question_type',
            },
        ),
        migrations.CreateModel(
            name='EducationBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=100)),
                ('board_status', models.CharField(default='Active', max_length=20)),
                ('board_created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('board_created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'education_board',
            },
        ),
        migrations.CreateModel(
            name='ClassManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_status', models.CharField(default='Active', max_length=20)),
                ('class_created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('class_created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'class_management',
            },
        ),
        migrations.CreateModel(
            name='ChapterManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=100)),
                ('chapter_status', models.CharField(default='Active', max_length=20)),
                ('chapter_created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('chapter_created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chapter_management',
            },
        ),
    ]
