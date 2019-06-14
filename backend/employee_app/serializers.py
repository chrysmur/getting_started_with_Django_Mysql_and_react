from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields = "__all__"

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields = "__all__"

class DeptEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeptEmp
        fields = "__all__"

class DeptManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeptManager
        fields = "__all__"

class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salaries
        fields = "__all__"

class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Titles
        fields = "__all__"