from django.urls import path
from . import views
from .views import save_callback, callback_success, property_list, login_view, book_property, make_payment, booking_success

urlpatterns = [
    path('', login_view, name='main_login'),
    path('home/', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('apply/', views.apply, name='apply'),
    path('callback/', save_callback, name='save_callback'),
    path('callback/success/', callback_success, name='callback_success'),
    path('properties/', property_list, name='property_list'),
    path('properties/book/', views.book_property, name='book_property'),
    path('payment/', make_payment, name='make_payment'),
    path('booking-success/', views.booking_success, name='booking_success'),


]




