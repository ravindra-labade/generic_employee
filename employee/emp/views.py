
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Employee

class Add_employee(CreateView):
    model = Employee
    fields = "__all__"


class List_employee(ListView):
    model = Employee

class Detail_employee(DetailView):
    model = Employee


class Update_employee(UpdateView):
    model = Employee

    fields = "__all__"
    success_url = "/"

class Delete_employee(DeleteView):
    model = Employee
    success_url = "/"
    template_name = "emp/Employee_confirm.html"


    