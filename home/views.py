import json
from django.http import JsonResponse
from django.shortcuts import render
from .services import analyze_resume


def home(request):
    return render(request, "home/index.html")


def resume_analysis(request):

    if request.method == "POST":

        resume_text = request.POST.get("resume_text")
        job_description = request.POST.get("job_description")

        result = analyze_resume(
            resume_text,
            job_description
        )

        return JsonResponse(result)

    return JsonResponse(
        {"error": "Invalid request"},
        status=400
    )