# Generated by Django 2.0.3 on 2018-04-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='imgLoc',
            field=models.CharField(default='default.jpg', max_length=20),
        ),
    ]
