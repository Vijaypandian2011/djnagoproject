from django.db import models
from django.utils import timezone


class Application(models.Model):
    Name = models.CharField(max_length=50)
    DateOfBirth = models.DateField()
    Age = models.IntegerField()
    EmailAddress = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    LinkedInUrl = models.URLField()
    Address = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdf_files/')


class CallbackRequest(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    property_type = models.CharField(max_length=20)
    budget = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    area = models.FloatField()
    property_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class LoginDetails(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    otp = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    pan_card_number = models.CharField(max_length=10)
    booked_at = models.DateTimeField(default=timezone.now)
    terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return self.name
