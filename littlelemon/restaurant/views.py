from django.shortcuts import render
from .forms import BookingForm

def booking_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'restaurant/booking.html', {'form': form})
    
