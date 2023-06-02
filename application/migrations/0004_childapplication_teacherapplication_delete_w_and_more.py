# Generated by Django 4.1.4 on 2023-05-28 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_w_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(max_length=50, verbose_name='Ваше Ф.И.О.')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('age', models.IntegerField(verbose_name='Возраст ребёнка')),
                ('need_in_logopedist', models.BooleanField(verbose_name='Нужен логопед')),
                ('need_in_psychologist', models.BooleanField(verbose_name='Нужен психолог')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(max_length=50, verbose_name='Ваше Ф.И.О.')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('education', models.CharField(max_length=50, verbose_name='Образование')),
                ('experience', models.CharField(max_length=50, verbose_name='Стаж работы')),
                ('specialization', models.TextField(verbose_name='Специальность')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='W',
        ),
        migrations.AlterField(
            model_name='question',
            name='phone_number',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона'),
        ),
    ]