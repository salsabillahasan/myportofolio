import uuid

from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    photo_url = models.URLField(blank=True, max_length=500)
    logo_image = models.ImageField(upload_to="experience/logos/", blank=True, null=True)
    photo_image = models.ImageField(upload_to="experience/photos/", blank=True, null=True)

    @property
    def logo_src(self):
        if self.logo_image:
            return self.logo_image.url
        return self.thumbnail or ""

    @property
    def photo_src(self):
        if self.photo_image:
            return self.photo_image.url
        return self.photo_url or ""
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    logo_image = models.ImageField(upload_to="education/logos/", blank=True, null=True)

    @property
    def logo_src(self):
        if self.logo_image:
            return self.logo_image.url
        return self.thumbnail or ""

    def __str__(self):
        return self.institution
    
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    project_image = models.ImageField(upload_to="projects/", blank=True, null=True)

    @property
    def image_src(self):
        if self.project_image:
            return self.project_image.url
        return self.project_image_url or ""

    @property
    def tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(",") if tech.strip()]
    
    def __str__(self):
        return self.title