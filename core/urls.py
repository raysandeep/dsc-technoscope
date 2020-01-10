from .views import DepartmentView, department_view

from django.urls import path

urlpatterns = [
    #path('',DepartmentView.as_view()),
    path('', department_view),
]
