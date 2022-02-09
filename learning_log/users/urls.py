from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Add default URL auth
    path('', include('django.contrib.auth.urls')),
]