from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('job.urls')),
    path('api/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view())
]

handler_404 = 'utils.error_views.handler_404'
handler_500 = 'utils.error_views.handler_500'

