from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "V-CAPE Administration"
admin.site.site_title = "V-CAPE Admin Portal"
admin.site.index_title = "Welcome to V-CAPE Dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
