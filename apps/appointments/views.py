from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from apps.services.models import Service


@login_required
def appointment_create(request, service_id=None):
    initial = {}
    if service_id:
        service = get_object_or_404(Service, pk=service_id, is_active=True)
        initial['service'] = service

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            messages.success(request, 'Вы успешно записались на приём!')
            return redirect('accounts:profile')
    else:
        form = AppointmentForm(initial=initial)

    return render(request, 'appointments/appointment_form.html', {'form': form})


@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user)
    if appointment.status != 'completed':
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Запись отменена.')
    else:
        messages.error(request, 'Нельзя отменить завершённую запись.')
    return redirect('accounts:profile')
