# Generated by Django 3.2.14 on 2022-07-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dept_name',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='role_name',
        ),
    ]
