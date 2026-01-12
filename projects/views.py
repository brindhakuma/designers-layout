from projects.models import Project
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Candidate

@login_required
def overview(request):
    total_projects = Project.objects.filter(user=request.user).count()

    return render(request, 'accounts/overview.html', {
        'total_projects': total_projects
    })

@login_required
def upload_project(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        Project.objects.create(
            user=request.user,
            title=uploaded_file.name,        # auto title
            category='General',               # default category
            file=uploaded_file
        )
    return redirect('overview')

# @login_required
# def publish_project(request):
#       if request.method == "POST":
#         # image = request.FILES.get('image')
#         title = request.POST.get('title')
#         category = request.POST.get('category')

#         if title and category:
#             Project.objects.create(
#                 user=request.user,
#                 title=title,
#                 category=category,

#             )

#         return redirect('products')


def new_project(request):
    return render(request, 'projects/new_project.html')

@login_required
def publish_project(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        old_price = request.POST.get('old_price') or None
        new_price = request.POST.get('new_price') or None

        if title and category:
            # ✅ 1. Save Project (for count)
            Project.objects.create(
                user=request.user,
                title=title,
                category=category,
            )

            # ✅ 2. Save Product (for products page)
            Product.objects.create(
                title=title,
                category=category,
                image=image,
                old_price=old_price,
                new_price=new_price,
            )

        # ✅ 3. Redirect to products page (NOT overview)
        return redirect('products')



def products(request):
    products = Product.objects.all()
    return render(request, 'projects/products.html', {
        'products': products
    })

def hirenow(request):
    return render(request, 'projects/hirenow.html')

def send_inquiry(request):
    if request.method == "POST":
        Candidate.objects.create(
            hiring_for=request.POST.get('hiring_for'),
            category=request.POST.get('category'),
            budget=request.POST.get('budget'),
            project_description=request.POST.get('project_description'),
            personal_note=request.POST.get('personal_note'),
            hiring_type=request.POST.get('hiring_type'),
        )
    return redirect('overview')


