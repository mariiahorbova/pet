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
    # Page for adding new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding new entry
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
]
