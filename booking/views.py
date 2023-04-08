from django.shortcuts import render, redirect
from .models import slot
from .forms import slotForm


def home(request):
    form = slotForm()
    context = {
        'form': form
    }

    return render(request, 'booking/booking_main.html', context)


def add(request):
    if request.method == 'POST':
        form = slotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    form = slotForm()
    context = {
        'form': form
    }

    return render(request, 'booking/booking_result.html', context)
