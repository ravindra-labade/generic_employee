from django.urls import path
from .views import Add_employee, List_employee, Detail_employee, Update_employee, Delete_employee

urlpatterns = [
    path('add/', Add_employee.as_view()),
    path('list/', List_employee.as_view()),
    path('detail/<int:pk>/', Detail_employee.as_view()),
    path('update/<int:pk>/', Update_employee.as_view()),
    path('delete/<int:pk>/', Delete_employee.as_view()),
]
