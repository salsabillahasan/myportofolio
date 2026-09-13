from django.test import TestCase
from django.urls import reverse

from .models import Education


class EducationPageTest(TestCase):

    def test_education_url_and_template(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")


    def test_education_data_appears_on_page(self):
        Education.objects.create(
            institution="Universitas Indonesia",
            degree="Bachelor's Degree",
            field_of_study="Information Systems",
            started_at="2025-08-01",
            ended_at=None,
            description="Information Systems undergraduate student."
        )

        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "Information Systems")


    def test_empty_education_message(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(
            response,
            "Belum ada pendidikan yang ditambahkan."
        )