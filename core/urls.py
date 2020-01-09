from .views import DepartmentView

from django.urls import path

urlpatterns = [
    path('',DepartmentView.as_view()),
]
