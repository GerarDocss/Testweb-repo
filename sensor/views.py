from django.shortcuts import render

# Create your views here.

def temperature(request):

    return render(request, 'sensor/about.html', {'title': 'Sensor'})

