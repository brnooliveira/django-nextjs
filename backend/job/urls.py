from django.urls import path
from job import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.createJob, name='create_job'),
    path('jobs/<str:pk>/', views.getOneJob, name='job'),
    path('jobs/<str:pk>/update/', views.updateJob, name='update_job'),
    path('jobs/<str:pk>/delete/', views.delete_job, name='delete_job')

]
