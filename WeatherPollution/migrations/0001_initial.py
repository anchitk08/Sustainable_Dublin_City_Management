# Generated by Django 2.1.5 on 2019-03-20 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station', models.CharField(max_length=50)),
                ('Temperature', models.IntegerField(null=True)),
                ('Weather', models.CharField(max_length=25, null=True)),
                ('WindSpeed', models.IntegerField(null=True)),
                ('WindGust', models.IntegerField(null=True)),
                ('WindDirection', models.CharField(max_length=10, null=True)),
                ('Humidity', models.IntegerField(null=True)),
                ('Rainfall', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('Pressure', models.IntegerField(null=True)),
                ('cm_last_insert_dttm', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]