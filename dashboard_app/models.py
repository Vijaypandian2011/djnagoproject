from django.db import models


class BookingAppointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.CharField(max_length=50)
    day = models.DateField()
    time = models.CharField(max_length=10)
    time_ordered = models.DateTimeField()
    user_id = models.IntegerField()


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()


class RegistrationAppApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    DateOfBirth = models.DateField()
    Age = models.IntegerField()
    EmailAddress = models.CharField(max_length=254)
    PhoneNumber = models.CharField(max_length=11)
    LinkedInUrl = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    pdf_file = models.CharField(max_length=100)


class RegistrationAppBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    pan_card_number = models.CharField(max_length=10)
    booked_at = models.DateTimeField()
    terms_and_conditions = models.BooleanField()
    property_id = models.BigIntegerField()


class RegistrationAppCallbackRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    property_type = models.CharField(max_length=20)
    budget = models.IntegerField()
    latitude = models.FloatField()
    timestamp = models.DateTimeField()
    booking_id = models.BigIntegerField()


class RegistrationAppProperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    area = models.FloatField()
    property_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
