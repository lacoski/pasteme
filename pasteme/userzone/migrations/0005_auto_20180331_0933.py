# Generated by Django 2.0 on 2018-03-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0004_auto_20180331_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='short_link',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]