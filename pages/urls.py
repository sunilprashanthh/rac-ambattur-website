# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_us_view, name='about'),
    path('team/', views.our_team_view, name='team'),
    path('projects/', views.projects_view, name='projects'), # Lists all projects

    # DYNAMIC URL for individual project details
    # It captures a 'slug' from the URL and passes it as 'project_slug' to the view
    path('projects/<slug:project_slug>/', views.project_detail_view, name='project_detail'),

    path('contact/', views.contact_us_view, name='contact'),
]