# Generated by Django 4.1.7 on 2023-03-27 10:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0002_alter_realtor_date_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('sale_type', models.CharField(choices=[('For Sale', 'Sale'), ('For Rent', 'Rent')], default='For Sale', max_length=50)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Studio Apartment', 'Studio Apartment'), ('Commercial Space', 'Commercial Space')], default='Apartment', max_length=100)),
                ('price', models.IntegerField()),
                ('bedrooms_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], null=True, verbose_name='Bedrooms')),
                ('bathrooms_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Bathrooms')),
                ('kitchens_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Kitchens')),
                ('balconies_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Balconies')),
                ('furnished', models.CharField(blank=True, choices=[('Semi-furnished', 'Semi Furnished'), ('Furnished with modern utilities', 'Furnished Modern'), ('Furnished with classic utilities', 'Furnished Classic'), ('Luxurious', 'Lux')], default='Furnished with modern utilities', max_length=100, verbose_name='Furnished')),
                ('parking', models.CharField(blank=True, choices=[('Garage', 'Garage'), ('Underground parking', 'Underground Garage'), ('Exterior parking', 'Exterior Parking'), ('Subscription parking', 'Subscription Parking')], default='Garage', max_length=100, verbose_name='Parking opportunity')),
                ('construction_year', models.IntegerField(blank=True, null=True, verbose_name='Construction year')),
                ('floor_number', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], null=True, verbose_name='Floor')),
                ('sqm', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('listing_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.realtor')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listings', verbose_name='Photo')),
            ],
        ),
    ]