from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404

from employees.models import Employee

# Create your views here.

def employee_detail(request, pk):

    employee = get_object_or_404(Employee, pk=pk)
    return HTTPResponse(employee)
