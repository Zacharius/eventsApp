# Generated by Django 2.0.5 on 2018-06-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0008_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='default slug', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]