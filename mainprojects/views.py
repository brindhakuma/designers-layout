from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ScrollImage
# from projects.models import Project
@login_required
def scroll_page(request):
    images = ScrollImage.objects.filter(user=request.user)
    print(images) 
    return render(request, 'mainprojects/scrollpage.html', {
        'images': images
    })


# @login_required
# def upload_scroll_image(request):
#     if request.method == 'POST':
#         image = request.FILES.get('image')

#         if image:
#             ScrollImage.objects.create(
#                 user=request.user,
#                 image=image
#             )

#     return redirect('scroll_page')

def upload_scroll_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        ScrollImage.objects.create(
            user=request.user,           
            image=request.FILES['image']
        )
    return redirect('scroll_page')


# def overview(request):
#     return render(request, 'accounts/overview.html')

def scroll_page(request):
    return render(request, 'mainprojects/scrollpage.html')

# def profile(request):
#     return render(request, 'occupation/profile.html')


# @login_required
# def overview(request):
#     total_projects = Project.objects.filter(user=request.user).count()
#     return render(request, 'mainprojects/overview.html', {
#         'total_projects': total_projects
#     })