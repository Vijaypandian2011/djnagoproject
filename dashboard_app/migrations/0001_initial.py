# Generated by Django 4.2.1 on 2023-06-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingAppointment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=50)),
                ('day', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('time_ordered', models.DateTimeField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationAppApplication',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField()),
                ('Age', models.IntegerField()),
                ('EmailAddress', models.CharField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=11)),
                ('LinkedInUrl', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('pdf_file', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationAppBooking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=254)),
                ('pan_card_number', models.CharField(max_length=10)),
                ('booked_at', models.DateTimeField()),
                ('terms_and_conditions', models.BooleanField()),
                ('property_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationAppCallbackRequest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=20)),
                ('property_type', models.CharField(max_length=20)),
                ('budget', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('booking_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationAppProperty',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('area', models.FloatField()),
                ('property_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
