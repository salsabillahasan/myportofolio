from django.urls import path

from main.views import delete_education, show_main, show_experience, show_education, show_projects, create_project, delete_project, create_education, update_education, delete_education, get_projects_json, get_education_json

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('education/', show_education, name='show_education'),
    path("education/add", create_education, name="create_education"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("education/update/<int:education_id>/edit/", update_education, name="update_education"),
    path("education/<int:education_id>/delete/", delete_education, name="delete_education"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/education/", get_education_json, name="get_education_json")
 
]