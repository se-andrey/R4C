from django.urls import path
from robots.views import add_robot, download_robot_summary

urlpatterns = [
    path('api/add_robot', add_robot, name='add_robot'),
    path('download_summary', download_robot_summary, name='download_robot_summary'),
]
