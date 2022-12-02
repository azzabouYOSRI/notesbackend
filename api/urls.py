from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('notes', views.get_notes),
    path('notes1/', views.create_note),
    path('notes/<str:pk>/', views.update_note),
    path('notes/delete/<str:pk>/', views.delete_note),
]
