import datetime

from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm, ExperienceForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST
from django.db.models import Q


def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "No login session yet / Cookie not found"
    )

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "npm": "2506548660",
        "study_program": "Information Systems",
        "bio": (
            "Information Systems student at Universitas Indonesia who enjoys exploring product management, technology, and creative problem-solving. I’m interested in understanding what people need, turning ideas into useful products, and learning how technology can create meaningful experiences."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
    }

    return render(request, "register.html", context)

def show_experience(request):
    is_editor = request.user.groups.filter(name="Editor").exists()

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "is_editor": is_editor,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    search_query = request.GET.get("q", "").strip()
    experiences = Experience.objects.prefetch_related("starred_by").order_by("-started_at")
    search_query = request.GET.get("q", "").strip()
    experiences = Experience.objects.prefetch_related("starred_by").order_by("-started_at")

    if search_query:
        experiences = experiences.filter(
            Q(title__icontains=search_query) | Q(role__icontains=search_query)
        )

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False

        start_label = experience.started_at.strftime("%b %Y")
        end_label = experience.ended_at.strftime("%b %Y") if experience.ended_at else "Present"

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "role": experience.role,
                "description": experience.description,
                "period": f"{start_label} — {end_label}",
                "photo_src": experience.photo_src,
                "logo_src": experience.logo_src,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": ", ".join([u.username for u in starred_users]),
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST, request.FILES)

    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    is_editor = request.user.groups.filter(name="Editor").exists()

    if not request.user.is_superuser and not is_editor:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None, request.FILES or None, instance=experience)

    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")


    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
        "experience": experience,
        "is_editor": is_editor,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    
    return redirect("main:show_experience")

def show_education(request):
    json_response = get_education_json(request)

    education_objects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )

    education_list = [
        education.object
        for education in education_objects
    ]

    is_editor = request.user.groups.filter(name="Editor").exists()

    context = {
        "education_list": education_list,
        "nickname": "Alsa",
        "name": "Salsabilla Hasan",
        "is_editor": is_editor,
    }

    return render(request, "education.html", context)   

@login_required(login_url="/login/") 
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education successfully added.")
        return redirect("main:show_education")

    context = {
        "name": "Salsabilla Hasan",
        "nickname" : "Alsa",
        "form" : form,
    }

    return render(request, "education_form.html", context)

@login_required(login_url="/login/") 
def update_education(request, education_id):    
    education = get_object_or_404(Education, pk=education_id)
    is_editor = request.user.groups.filter(name="Editor").exists()

    form = EducationForm(request.POST or None, request.FILES or None, instance=education)

    if not request.user.is_superuser and not is_editor:
        raise PermissionDenied

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education successfully updated!")
        return redirect("main:show_education")

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
        "education": education,
        "is_editor": is_editor
    }

    return render(request, "education_form.html", context)

@login_required(login_url="/login/") 
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education successfully deleted!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def show_projects(request):
    title_query = request.GET.get("title", "").strip()
    is_editor = request.user.groups.filter(name="Editor").exists()

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/") 
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    is_editor = request.user.groups.filter(name="Editor").exists()

    if not request.user.is_superuser and not is_editor:
        raise PermissionDenied

    form = ProjectForm(request.POST or None, request.FILES or None,instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
        "project": project,
        "is_editor": is_editor
    }

    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "tech_list": project.tech_list,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "image_src": project.image_src,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/") 
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_education_json(request):
    education = Education.objects.all()
    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response    

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST, request.FILES)

    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)