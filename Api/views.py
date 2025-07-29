from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from Api.models import Company,Empolyee
from Api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action # type: ignore
from rest_framework.response import Response # type: ignore
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class=CompanySerializer
    
    # url={companies/{company_id}/employees}
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        print("get employees of ",pk,"company")
        try:
          company=Company.objects.get(pk=pk)
          emps=Empolyee.objects.filter(company=company)
          emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                "message":"Company might not exists !! Error "
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Empolyee.objects.all()
    serializer_class = EmployeeSerializer
