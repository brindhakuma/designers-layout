# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from projects.models import Project


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return render(request, 'accounts/overview.html')
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, 'accounts/login.html')


# @login_required
# def overview(request):
#     total_projects = Project.objects.filter(user=request.user).count()
#     print("TOTAL PROJECTS:", total_projects)  # DEBUG

#     return render(request, 'accounts/overview.html', {
#         'total_projects': total_projects
#     })


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.models import Candidate

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('overview')   # ✅ redirect ONLY
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')


@login_required
def overview(request):
    total_projects = Project.objects.filter(user=request.user).count()
    # print("OVERVIEW VIEW CALLED — TOTAL:", total_projects)
    total_candidates = Candidate.objects.count() 

    return render(request, 'accounts/overview.html', {
        'total_projects': total_projects,
        'total_candidates': total_candidates,
    })


