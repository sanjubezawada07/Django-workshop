# Generated by Django 3.2 on 2024-02-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BSApp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='edesg',
            field=models.CharField(choices=[('0', '--select designation--'), ('1', 'Intern'), ('2', 'junior trainee'), ('3', 'junior developer')], default='0', max_length=5),
        ),
    ]
