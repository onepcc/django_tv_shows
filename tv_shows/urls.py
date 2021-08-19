from django.urls import path
from . import views
urlpatterns = [
        path('', views.inicio),
        path('shows', views.shows),
        path('shows/new/', views.index),
        path('shows/<int:val>', views.ver_show),
        path('shows/<int:val>/edit', views.edit_show),
        path('shows/<int:val>/update', views.update_show),
        path('shows/<int:val>/borrar', views.delete_show),
        
]
