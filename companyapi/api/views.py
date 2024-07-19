from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Django Rest throw
from api.models import Company , Employee
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import CompanySerializers , EmployeeSerializers
class CompnayViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


    # compnies/{companyid}/employees
    # http://127.0.0.1:8000/api/v1/companies/2/employees/
    # We Fetch All Empoyee on Particaular Orginzation and Custom Url Created Concept
    @action(detail = True , methods = ['get'])
    def employees(self , request , pk = None):
        print("Get emppiyee data solve")
        company = Company.objects.get(pk = pk)
        emps = Employee.objects.filter(company=company)
        emps_seralizer =   EmployeeSerializers(emps , many=True , context = {"request":request})

        return  Response(emps_seralizer.data)

# Empoyee View
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
