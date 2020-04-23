from django.shortcuts import render, redirect
from projects.models import Listing_Database
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatingListingForm
from .filters import ItemFilter

def project_index(request):
    projects = Listing_Database.objects.all()

    myFilter = ItemFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    context = {
        'projects': projects, 'myFilter': myFilter,
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Listing_Database.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

@login_required
def createListing(request):
    if request.method == 'POST':
        listing_form = CreatingListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            link  = listing_form.save(commit=False)
            link.user = request.user
            link.save()
            messages.success(request, f'Your listing has been created!!')
            return redirect('/portal/')
    else:
        listing_form = CreatingListingForm()
        link = listing_form
    return render(request, 'createListing.html', {'listing_form': link})


