from django.urls import path
from .views import dashboard_view

app_name = 'dashboard_app'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
