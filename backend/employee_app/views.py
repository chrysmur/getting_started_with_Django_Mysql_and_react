from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

class EmployeeAPI(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()[:5]

class DepartmentsAPI(viewsets.ModelViewSet):
    serializer_class = DepartmentsSerializer
    queryset = Departments.objects.all()[:5]

class DeptManagerAPI(viewsets.ModelViewSet):
    serializer_class = DeptManagerSerializer
    queryset = DeptManager.objects.all()[:5]

class DeptEmpAPI(viewsets.ModelViewSet):
    serializer_class = DeptEmpSerializer
    queryset = DeptEmp.objects.all()[:5]

class SalariesAPI(viewsets.ModelViewSet):
    serializer_class = SalariesSerializer
    queryset = Salaries.objects.all()[:5]
    
class TitlesAPI(viewsets.ModelViewSet):
    serializer_class = TitlesSerializer
    queryset = Titles.objects.all()[:5]