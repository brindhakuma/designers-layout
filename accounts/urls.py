from django.urls import path
from .views import login_view
from .views import overview

urlpatterns = [
    path('login/', login_view, name='login'),
     path('overview/', overview, name='overview'),
]
