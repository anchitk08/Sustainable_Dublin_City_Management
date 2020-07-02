# Generated by Django 2.1.5 on 2019-03-20 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametext', models.CharField(max_length=500)),
                ('descriptiontext', models.CharField(max_length=1500)),
                ('organization_id', models.BigIntegerField()),
                ('online_event', models.CharField(max_length=500)),
                ('startutc', models.DateTimeField(verbose_name='startutc')),
                ('endutc', models.DateTimeField(verbose_name='endutc')),
                ('listed', models.BooleanField()),
                ('is_free', models.BooleanField()),
                ('url', models.CharField(max_length=500)),
                ('resource_uri', models.CharField(max_length=500)),
                ('cm_last_insert_dttm', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]