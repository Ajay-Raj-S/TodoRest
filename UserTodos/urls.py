from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('todo/', TodoList.as_view()),
    path('todo/<int:pk>/', TodoManage.as_view()),
]