from django.urls import path
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from main.views import (
    delete_education, 
    show_main, 
    show_experience, 
    show_education, 
    show_projects, 
    create_project, 
    delete_project, 
    create_education, 
    toggle_star, 
    update_education, 
    delete_education, 
    get_projects_json, 
    get_education_json, 
    register, 
    login_user, 
    logout_user,
    update_project,
    create_experience,
    update_experience,
    delete_experience,
    create_project_ajax,
    toggle_experience_star,
    get_experience_json,
    create_experience_ajax
)

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
    path("api/education/", get_education_json, name="get_education_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/<uuid:project_id>/edit/", update_project, name="update_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("experience/<uuid:experience_id>/star/", toggle_experience_star, name="toggle_experience_star"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]