from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.appointments.models import Appointment
from apps.services.models import Service

User = get_user_model()


class AppointmentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='patient',
            email='patient@test.com',
            password='pass123',
            phone='+79991234567'
        )
        self.service = Service.objects.create(
            name="МРТ",
            category="mri",
            price=3500,
            description="Тест",
            is_active=True
        )

    def test_appointment_creation(self):
        appointment = Appointment.objects.create(
            patient=self.user,
            service=self.service,
            appointment_date=timezone.now() + timezone.timedelta(days=1),
            status='pending'
        )
        self.assertEqual(appointment.status, 'pending')
        self.assertEqual(appointment.patient.username, 'patient')

    def test_appointment_create_view_requires_login(self):
        response = self.client.get(reverse('appointments:appointment_create'))
        self.assertEqual(response.status_code, 302)

    def test_appointment_create_view_authenticated(self):
        self.client.login(username='patient', password='pass123')
        response = self.client.get(reverse('appointments:appointment_create'))
        self.assertEqual(response.status_code, 200)

    def test_appointment_cancel_view(self):
        self.client.login(username='patient', password='pass123')
        appointment = Appointment.objects.create(
            patient=self.user,
            service=self.service,
            appointment_date=timezone.now() + timezone.timedelta(days=1),
            status='pending'
        )
        self.client.post(reverse('appointments:appointment_cancel', args=[appointment.id]))
        appointment.refresh_from_db()
        self.assertEqual(appointment.status, 'cancelled')
