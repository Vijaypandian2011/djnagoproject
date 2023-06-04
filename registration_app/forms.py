from django import forms
from .models import CallbackRequest,  Booking, Payment


class ApplicationForm(forms.Form):
    Name = forms.CharField(max_length=50)
    DateOfBirth = forms.DateField()
    Age = forms.IntegerField()
    EmailAddress = forms.EmailField()
    PhoneNumber = forms.CharField(max_length=11)
    LinkedInUrl = forms.URLField()
    Address = forms.CharField(max_length=200)
    pdf_file = forms.FileField()


class CallbackRequestForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'contact', 'property_type', 'budget', 'latitude', 'longitude']


class LoginForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=10, required=True)
    otp = forms.CharField(max_length=4, required=True)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != 10:
            raise forms.ValidationError('Phone number should be 10 characters long.')
        return phone_number

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Name should not contain numbers.')
        return name

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        if not otp.isdigit() or len(otp) != 4:
            raise forms.ValidationError('OTP should be a 4-digit number.')
        return otp


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'email', 'pan_card_number', 'terms_and_conditions']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_holder_name', 'card_number', 'otp']