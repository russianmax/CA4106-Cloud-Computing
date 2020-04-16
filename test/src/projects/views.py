from django.shortcuts import render, redirect
from projects.models import Listing_Database
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def project_index(request):
    projects = Listing_Database.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

