# Generated by Django 3.2.4 on 2021-06-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='create_datetime',
            field=models.DateTimeField(default=False),
        ),
    ]
