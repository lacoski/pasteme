# Generated by Django 2.0.2 on 2018-03-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='short_link',
            field=models.TextField(),
        ),
    ]