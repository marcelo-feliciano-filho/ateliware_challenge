from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'templates/home.html', {'jobs': 'jobs'})

def detail(request, job_id):
    return render(request, 'jobs/detail.html', {'job': 'job_detail'})
