from django.shortcuts import render, redirect
from .models import slot


def home(request):

    return render(request, 'booking/booking_main.html')
