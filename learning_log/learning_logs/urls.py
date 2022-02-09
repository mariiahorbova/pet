""" Defines URL patterns for learning_logs """

from django.urls import path

from . import views

app_name = "Learning_logs"
urlpatterns = [
    # Main page
    path("", views.index, name="index"),
    # Page of all topics
    path("topics/", views.topics, name="topics"),
    # Page of a specific topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
