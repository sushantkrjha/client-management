from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('job-sheet/create/', views.create_job_sheet, name='create_job_sheet'),
    path('job-sheet/<int:id>/edit/', views.edit_job_sheet, name='edit_job_sheet'),
    path('job-sheet/<int:id>/', views.view_job_sheet, name='view_job_sheet'),
    path('delete/<int:id>/', views.delete_job_sheet, name='delete_job_sheet'),
]
