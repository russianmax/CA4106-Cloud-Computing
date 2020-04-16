from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def project_index(request):
    context = {
    }
    return render(request, 'project_index.html', context)

