from django.urls import path
from robots.views import add_robot, get_csrf_token

urlpatterns = [
    path('api/add_robot', add_robot, name='add_robot'),
]