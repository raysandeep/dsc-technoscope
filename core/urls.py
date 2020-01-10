from .views import DepartmentView, department_view, Health

from django.urls import path

urlpatterns = [
    #path('',DepartmentView.as_view()),
    path('', department_view),
    path('check/', Health.as_view()),
]
