from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import ApplicationForm, CallbackRequestForm, LoginForm, BookingForm, PaymentForm
from .models import Application as AppModel, Property, LoginDetails, Booking, Payment
from django.utils import timezone


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = AppModel(
                Name=form.cleaned_data['Name'],
                DateOfBirth=form.cleaned_data['DateOfBirth'],
                Age=form.cleaned_data['Age'],
                EmailAddress=form.cleaned_data['EmailAddress'],
                PhoneNumber=form.cleaned_data['PhoneNumber'],
                LinkedInUrl=form.cleaned_data['LinkedInUrl'],
                Address=form.cleaned_data['Address'],
                pdf_file=request.FILES['pdf_file']
            )
            application.save()
            success_message = 'Successfully Applied!'
            return render(request, 'popup.html', {'form': form, 'success_message': success_message})
    else:
        form = ApplicationForm()

    applications = AppModel.objects.all()

    return render(request, 'apply.html', {'form': form, 'applications': applications})


def save_callback(request):
    if request.method == 'POST':
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('callback_success')
    else:
        form = CallbackRequestForm()
    return render(request, 'callback.html', {'form': form})


def callback_success(request):
    return render(request, 'popup.html')


def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'properties.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            otp = form.cleaned_data['otp']

            # Validating the OTP (dummy logic, any 4-digit number is accepted)
            if otp and otp.isdigit() and len(otp) == 4:
                # OTP is valid, update login details in the database
                login_time = timezone.now()
                login_details = LoginDetails(name=name, phone_number=phone_number, login_time=login_time)
                login_details.save()

                # Display success message
                success_message = 'Login Successful!'
                return render(request, 'home.html', {'form': form, 'success_message': success_message})
            else:
                # Invalid OTP, display error message
                error_message = 'Invalid OTP'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def book_property(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            return render(request, 'payment.html', {'form': PaymentForm, 'booking_id': Booking.phone_number})
    else:
        form = BookingForm()

    return render(request, 'bookingap.html', {'form': form})


def make_payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            return redirect('booking_success')
    else:
        return HttpResponseBadRequest()


def booking_success(request):
    return render(request, 'popup.html')