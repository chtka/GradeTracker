# Generated by Django 2.0.7 on 2018-07-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180726_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=30),
        ),
    ]
