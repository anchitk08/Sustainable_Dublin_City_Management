# Generated by Django 2.1.7 on 2019-04-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherPollution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('Temperature', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('WindSpeed', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
            ],
        ),
    ]
