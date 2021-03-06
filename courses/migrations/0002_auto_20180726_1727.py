# Generated by Django 2.0.7 on 2018-07-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='institution',
            field=models.CharField(default='University of California, San Diego', max_length=254),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('department', 'number')},
        ),
    ]
