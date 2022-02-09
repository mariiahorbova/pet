from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs'))
]
