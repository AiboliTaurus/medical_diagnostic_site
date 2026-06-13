from django import forms
from .models import Appointment
from apps.services.models import Service
from apps.pages.models import Doctor


class AppointmentForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_service'})
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.none(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_doctor'}),
        label='Врач (опционально)'
    )
    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'id': 'id_appointment_date'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['service', 'doctor', 'appointment_date', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Если передан ID услуги (например, при редактировании)
        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['doctor'].queryset = Doctor.objects.filter(services__id=service_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.service:
            self.fields['doctor'].queryset = self.instance.service.doctor_set.all()
