# Generated by Django 2.0 on 2018-03-31 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0003_auto_20180330_0746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paste',
            options={'ordering': ['-time_create']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-time_create']},
        ),
        migrations.AlterField(
            model_name='paste',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='paste',
            name='time_end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_end',
            field=models.DateTimeField(auto_now=True),
        ),
    ]