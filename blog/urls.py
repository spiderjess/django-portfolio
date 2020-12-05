from . import views
from django.urls import path



urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]