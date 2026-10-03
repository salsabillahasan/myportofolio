from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput
from django.utils.html import strip_tags

from main.models import Project, Education, Experience

def strip_html(value):
    return strip_tags(value or "").strip()

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
            "project_image",
        ]

        labels = {
            "title": "Title",
            "description": "Description",
            "tech_stack": "Tech Stack",
            "project_url": "Project URL",
            "project_image": "Upload Project Image",
            "project_image_url": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    
class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "field_of_study",
            "started_at",
            "ended_at",
            "description",
            "thumbnail",
        ]

        labels = {
            "institution": "Institution",
            "degree": "Degree",
            "field_of_study": "Field of Study",
            "started_at": "Started At",
            "ended_at": "Ended At",
            "description": "Description",
            "thumbnail": "Logo",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": Textarea(
                attrs={
                    "placeholder": "Bachelor's Degree",
                    "rows": 3,
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "Information Systems",
                }
            ),
            "started_at": DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                }
            ),
            "description": TextInput(
                attrs={
                    "placeholder": "Tell us about your education experience",
                }
            ),
            "description": TextInput(
                attrs={ 
                    "placeholder": "Tell us about your education experience",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "role",
            "category",
            "started_at",
            "ended_at",
            "description",
            "logo_image",
            "thumbnail",
            "photo_image",
            "photo_url",
        ]
        labels = {
            "title": "Organization / Event",
            "role": "Role",
            "category": "Category",
            "started_at": "Start Date",
            "ended_at": "End Date (leave empty if still ongoing)",
            "description": "Description",
            "logo_image": "Upload Logo",
            "thumbnail": "…or Logo URL",
            "photo_image": "Upload Activity Photo",
            "photo_url": "…or Activity Photo URL",
        }
        widgets = {
            "started_at": DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "ended_at": DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "description": Textarea(attrs={"rows": 5}),
        }
    
    def clean_title(self):
        title = strip_html(self.cleaned_data["title"])
        if not title:
            raise ValidationError("Nama organisasi/event tidak boleh hanya berisi tag HTML.")
        return title

    def clean_role(self):
        role = strip_html(self.cleaned_data["role"])
        if not role:
            raise ValidationError("Role tidak boleh hanya berisi tag HTML.")
        return role

    def clean_description(self):
        description = strip_html(self.cleaned_data["description"])
        if not description:
            raise ValidationError("Deskripsi tidak boleh hanya berisi tag HTML.")
        return description

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("started_at")
        end = cleaned.get("ended_at")
        if start and end and end < start:
            self.add_error("ended_at", "End date cannot be earlier than start date.")
        return cleaned