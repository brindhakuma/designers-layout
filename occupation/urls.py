from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    # path('overview/', views.overview_view, name='overview'),
]
