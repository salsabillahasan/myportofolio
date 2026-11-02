
from datetime import date

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework.test import APITestCase

from main.models import Experience


class ExperienceAPITest(APITestCase):

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner_exp",
            email="owner@example.com",
            password="test-password",
        )

        self.editor = User.objects.create_user(
            username="editor_exp",
            password="test-password",
        )

        self.visitor = User.objects.create_user(
            username="visitor_exp",
            password="test-password",
        )

        editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(editor_group)

        self.experience = Experience.objects.create(
            title="Test Organization",
            role="Intern",
            category="internship",
            started_at=date(2026, 1, 1),
            description="Test experience",
        )

        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse(
            "api:experience-detail",
            args=[self.experience.id],
        )
        self.star_url = reverse(
            "api:experience-star",
            args=[self.experience.id],
        )

        self.payload = {
            "title": "New Experience",
            "role": "Developer",
            "category": "internship",
            "started_at": "2026-02-01",
            "description": "New test experience",
        }

    def test_public_can_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 2)

    def test_editor_can_patch(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"role": "Senior Intern"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.role,
            "Senior Intern",
        )

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.assertTrue(
            Experience.objects.filter(
                pk=self.experience.id
            ).exists()
        )

    def test_visitor_cannot_modify(self):
        self.client.force_authenticate(user=self.visitor)

        response = self.client.patch(
            self.detail_url,
            {"role": "Changed"},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

    def test_owner_can_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Experience.objects.filter(
                pk=self.experience.id
            ).exists()
        )

    def test_star_requires_login_and_toggles(self):
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(user=self.visitor)

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)
