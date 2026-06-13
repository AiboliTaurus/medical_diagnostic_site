from django.test import TestCase
from django.urls import reverse
from apps.feedback.models import ContactMessage


class FeedbackTest(TestCase):
    def test_contact_message_creation(self):
        message = ContactMessage.objects.create(
            name="Иван Петров",
            email="ivan@test.com",
            phone="+79991234567",
            message="Тестовое сообщение"
        )
        self.assertEqual(message.name, "Иван Петров")
        self.assertTrue(str(message).startswith("Сообщение от Иван Петров"))

    def test_contact_form_submission(self):
        response = self.client.post(reverse('pages:home'), {
            'name': 'Тест Тестов',
            'email': 'test@test.com',
            'phone': '+79991112233',
            'message': 'Привет, это тест!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(email='test@test.com').exists())
