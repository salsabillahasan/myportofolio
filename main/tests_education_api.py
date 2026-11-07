
from datetime import datetime

from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APITestCase, APIClient

from main.models import Education


class EducationAPITest(APITestCase):

    def setUp(self):
        # Membuat akun sementara untuk testing
        self.owner = User.objects.create_superuser(
            username="owner_edu",
            email="owner@example.com",
            password="test-password",
        )

        self.editor = User.objects.create_user(
            username="editor_edu",
            password="test-password",
        )

        self.visitor = User.objects.create_user(
            username="visitor_edu",
            password="test-password",
        )

        # Memasukkan akun Editor ke grup Editor
        editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(editor_group)

        # Membuat satu data Education untuk pengujian
        self.education = Education.objects.create(
            institution="Test University",
            degree="Bachelor",
            field_of_study="Information Systems",
            started_at=timezone.make_aware(
                datetime(2026, 1, 1, 9, 0)
            ),
            description="Test education",
        )

        # Alamat endpoint API Education
        self.list_url = reverse("api:education-list")

        self.detail_url = reverse(
            "api:education-detail",
            args=[self.education.id],
        )

        self.star_url = reverse(
            "api:education-star",
            args=[self.education.id],
        )

        # Contoh data untuk membuat Education
        self.payload = {
            "institution": "New University",
            "degree": "Bachelor",
            "field_of_study": "Computer Science",
            "started_at": "2026-02-01T09:00:00+07:00",
            "description": "New education",
        }

    # 1. Semua pengguna boleh melihat Education
    def test_public_can_view_and_search(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            self.list_url,
            {"q": "Test University"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"q": "Tidak Ada"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    # 2. Superuser boleh menambah Education
    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Education.objects.count(), 2)

    # 3. Superuser boleh mengubah dan menghapus
    def test_owner_can_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.patch(
            self.detail_url,
            {"degree": "Master"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(self.education.degree, "Master")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Education.objects.filter(
                pk=self.education.id
            ).exists()
        )

    # 4. Editor boleh mengubah Education
    def test_editor_can_patch(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"degree": "Updated Bachelor"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.degree,
            "Updated Bachelor",
        )

    # 5. Editor tidak boleh menambah atau menghapus
    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        initial_count = Education.objects.count()

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            Education.objects.count(),
            initial_count,
        )

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.assertTrue(
            Education.objects.filter(
                pk=self.education.id
            ).exists()
        )

    # 6. User biasa tidak boleh mengelola Education
    def test_regular_user_cannot_modify(self):
        self.client.force_authenticate(user=self.visitor)

        original_degree = self.education.degree
        initial_count = Education.objects.count()

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.patch(
            self.detail_url,
            {"degree": "Changed"},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.education.refresh_from_db()
        self.assertEqual(self.education.degree, original_degree)
        self.assertEqual(
            Education.objects.count(),
            initial_count,
        )

    # 7. Guest tidak boleh mengubah data
    def test_guest_cannot_modify(self):
        original_degree = self.education.degree

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.patch(
            self.detail_url,
            {"degree": "Changed"},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.education.refresh_from_db()
        self.assertEqual(self.education.degree, original_degree)
        self.assertEqual(Education.objects.count(), 1)

    # 8. Nama institusi kosong harus ditolak
    def test_invalid_institution_is_rejected(self):
        self.client.force_authenticate(user=self.owner)

        data = self.payload.copy()
        data["institution"] = "<b> </b>"

        response = self.client.post(
            self.list_url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("institution", response.data)
        self.assertEqual(Education.objects.count(), 1)

    # 9. Tanggal selesai tidak boleh sebelum mulai
    def test_invalid_date_is_rejected(self):
        self.client.force_authenticate(user=self.owner)

        data = self.payload.copy()
        data["started_at"] = "2026-05-01T09:00:00+07:00"
        data["ended_at"] = "2026-01-01T09:00:00+07:00"

        response = self.client.post(
            self.list_url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("ended_at", response.data)
        self.assertEqual(Education.objects.count(), 1)

    # 10. HTML pada nama institusi harus dibersihkan
    def test_html_tags_are_removed(self):
        self.client.force_authenticate(user=self.owner)

        data = self.payload.copy()
        data["institution"] = "<b>New University</b>"

        response = self.client.post(
            self.list_url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["institution"],
            "New University",
        )

    # 11. Star hanya boleh untuk akun login
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

    # 12. Request tanpa CSRF harus ditolak
    def test_csrf_is_required(self):
        csrf_client = APIClient(enforce_csrf_checks=True)

        logged_in = csrf_client.login(
            username="visitor_edu",
            password="test-password",
        )
        self.assertTrue(logged_in)

        response = csrf_client.post(self.star_url)

        self.assertEqual(response.status_code, 403)

        self.assertFalse(
            self.education.starred_by.filter(
                pk=self.visitor.pk
            ).exists()
        )


    def test_owner_can_clear_education_logo(self):
        self.education.logo_image = "education/logos/test.jpg"
        self.education.save(update_fields=["logo_image"])

        self.client.force_authenticate(user=self.owner)

        response = self.client.patch(
            self.detail_url,
            {"clear_logo_image": True},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertFalse(self.education.logo_image)
