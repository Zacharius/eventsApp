# Generated by Django 2.0.3 on 2018-04-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20180403_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='imgLoc',
            field=models.CharField(default='default.jpg', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=100),
        ),
    ]