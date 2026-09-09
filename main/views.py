from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "npm": "2506548660",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia who enjoys exploring product management, technology, and creative problem-solving. I’m interested in understanding what people need, turning ideas into useful products, and learning how technology can create meaningful experiences."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salsabilla Hasan",
        "nickname": "Alsa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)