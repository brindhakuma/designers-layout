from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import new_project

urlpatterns = [
    path('publish/', views.publish_project, name='publish_project'),
    path('new/', views.new_project, name='new_project'),
    path('products/', views.products, name='products'),
    path('hirenow/', views.hirenow, name='hirenow'),
    
    path('send-inquiry/', views.send_inquiry, name='send_inquiry'),

]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)