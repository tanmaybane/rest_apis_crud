# Generated by Django 3.2.4 on 2021-06-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20210621_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='update_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]