# Generated by Django 2.0.7 on 2018-08-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('points_total', models.FloatField()),
                ('points_earned', models.FloatField()),
            ],
        ),
    ]
