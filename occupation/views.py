from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from projects.models import Project

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Redirect to overview page after submission
    else:
        form = ProfileForm()
    return render(request, 'occupation/profile.html', {'form': form})

# def overview_view(request):
#     total_candidates = Profile.objects.count()  # Count of profiles submitted
#     return render(request, 'accounts/overview.html', {'total_projects': total_candidates})

def overview_view(request):
    total_projects = Project.objects.count()  # your existing total projects
    total_candidates = Profile.objects.count()  # new: count of submitted profiles

    return render(request, 'accounts/overview.html', {
        'total_projects': total_projects,
        'total_candidates': total_candidates,
    })