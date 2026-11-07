from django.test import TestCase
from django.urls import reverse

from .models import Education


class EducationPageTest(TestCase):
      
    def setUp(self):
        self.education = Education.objects.create(
            institution="Test University",
            degree="Bachelor",
            field_of_study="Information Systems",
            description="Test education",
        )

    def test_education_url_and_template(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_data_appears_on_page(self):
        response = self.client.get(
            reverse("main:show_education")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="education-list"')

        api_response = self.client.get(
            reverse("api:education-list")
        )

        self.assertEqual(api_response.status_code, 200)


        education_data = api_response.json()

        self.assertGreater(
            len(education_data),
            0
        )

        self.assertTrue(
            any(
                item["id"] == self.education.id
                for item in education_data
            )
        )


    def test_empty_education_message(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(
            response,
            "No education added yet."
        )