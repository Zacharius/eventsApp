# Generated by Django 2.0.5 on 2018-06-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_auto_20180430_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='default slug', max_length=100),
        ),
    ]
