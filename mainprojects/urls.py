from django.urls import path
from .views import scroll_page, upload_scroll_image
from . import views

urlpatterns = [
    path('scroll/', scroll_page, name='scroll_page'),
    path('upload-image/', upload_scroll_image, name='upload_scroll_image'),
    # path('overview/', views.overview, name='overview'),
    path('projects/', views.scroll_page, name='projects'),
    # path('profile/', views.profile, name='profile'),

]
