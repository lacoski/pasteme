# Generated by Django 2.0.2 on 2018-03-30 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0002_auto_20180330_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role_name',
            new_name='name_role',
        ),
    ]
