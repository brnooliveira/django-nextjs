from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.get_all_jobs, name='jobs'),
    path('jobs/new/', views.create_job, name='create_job'),
    path('jobs/<str:pk>/', views.get_one_job, name='job'),
    path('jobs/<str:pk>/update/', views.update_job, name='update_job'),
    path('jobs/<str:pk>/delete/', views.delete_job, name='delete_job')

]
