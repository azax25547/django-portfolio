from django.shortcuts import render
from .models import Job

# Create your views here.
def home(req):
    jobs = Job.objects
    return render(req, "jobs/home.html", {"jobs": jobs})
