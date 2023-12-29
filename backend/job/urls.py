from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.get_all_jobs, name='jobs'),
    path('jobs/new/', views.create_job, name='create_job'),
    path('jobs/<str:pk>/', views.get_one_job, name='job'),
    path('jobs/<str:pk>/update/', views.update_job, name='update_job'),
    path('jobs/<str:pk>/delete/', views.delete_job, name='delete_job'),
    path('job/<str:id>/apply/', views.apply_to_job, name='apply_to_job'),
    path('me/jobs/applied/', views.get_current_user_applied_jobs, name='current_user_applied_jobs'),
    path('me/jobs/', views.get_curent_user_jobs, name='get_curent_user_jobs'),
    path('jobs/<str:pk>/check/', views.is_applied, name='is_applied_to_job'),
    path('jobs/<str:pk>/candidates/', views.get_candidates_applied, name='get_candidates_applied'),

]
