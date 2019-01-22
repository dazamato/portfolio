from django.shortcuts import render
from .models import Job
from courses.models import Course

def home(request):
    jobs = Job.objects
    courses=Course.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'courses': courses})
