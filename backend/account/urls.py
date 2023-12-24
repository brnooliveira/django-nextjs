from account import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('me/', views.current_user, name='current_user')
]
