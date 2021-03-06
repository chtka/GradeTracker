# Generated by Django 2.0.7 on 2018-08-03 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professors', '0001_initial'),
        ('courses', '0003_auto_20180726_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(choices=[('FA', 'Fall'), ('WI', 'Winter'), ('SP', 'Spring'), ('SS1', 'Summer Session 1'), ('SS2', 'Summer Session 2')], max_length=10)),
                ('year', models.IntegerField()),
                ('grade', models.FloatField(default=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.Professor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
