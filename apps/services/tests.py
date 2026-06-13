from django.test import TestCase
from django.urls import reverse
from apps.services.models import Service


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name="МРТ головного мозга",
            category="mri",
            price=3500,
            description="Магнитно-резонансная томография головного мозга",
            is_active=True
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, "МРТ головного мозга")
        self.assertEqual(self.service.price, 3500)
        self.assertTrue(self.service.is_active)

    def test_service_str_method(self):
        self.assertEqual(str(self.service), "МРТ головного мозга - 3500 ₽")

    def test_service_list_view(self):
        response = self.client.get(reverse('services:service_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "МРТ головного мозга")

    def test_service_detail_view(self):
        response = self.client.get(reverse('services:service_detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Магнитно-резонансная томография")
