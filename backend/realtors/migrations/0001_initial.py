# Generated by Django 4.1.7 on 2023-03-24 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('top_seller', models.BooleanField(default=False)),
                ('date_hired', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 24, 17, 54, 56, 510204))),
            ],
        ),
    ]