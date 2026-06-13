from django.test import TestCase
from django.urls import reverse
from apps.pages.models import CompanyInfo, Doctor
from apps.services.models import Service


class CompanyInfoTest(TestCase):
    def setUp(self):
        self.company = CompanyInfo.objects.create(
            history="История компании",
            mission="Наша миссия",
            address="г. Москва, ул. Тестовая, 1",
            phone="+7 (999) 123-45-67",
            email="test@test.ru"
        )

    def test_company_creation(self):
        self.assertEqual(self.company.address, "г. Москва, ул. Тестовая, 1")
        self.assertEqual(str(self.company), "Информация о компании")

    def test_home_page_view(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_view(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_view(self):
        response = self.client.get(reverse('pages:contacts'))
        self.assertEqual(response.status_code, 200)


class DoctorTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name="МРТ",
            category="mri",
            price=3500,
            description="Тест",
            is_active=True
        )
        self.doctor = Doctor.objects.create(
            name="Иван Иванов",
            specialty="Рентгенолог",
            bio="Опытный врач",
            order=1
        )
        self.doctor.services.add(self.service)

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Иван Иванов")
        self.assertEqual(str(self.doctor), "Иван Иванов")

    def test_doctor_has_service(self):
        self.assertIn(self.service, self.doctor.services.all())
