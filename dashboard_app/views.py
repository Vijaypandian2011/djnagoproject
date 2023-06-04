from django.shortcuts import render
from .models import BookingAppointment
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64


def save_plot_to_image():
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    buf.close()
    return urllib.parse.quote(string)

def dashboard_view(request):
    # Fetch data from the database
    appointments = BookingAppointment.objects.all()

    # Create a pandas DataFrame from the fetched data
    df = pd.DataFrame(list(appointments.values()))

    if not df.empty:
        # Generate insights and summary statistics
        insights = df.describe()
    else:
        insights = None

    # Pass the data, insights, and other required variables to the template
    context = {
        'data': df.to_html(),
        'insights': insights.to_html() if insights else None,
        'graph_image': None,  # Replace with the generated graph image
    }

    return render(request, 'dashboard.html', context)
