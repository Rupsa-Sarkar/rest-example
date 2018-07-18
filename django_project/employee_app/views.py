from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from employee_app.models import Employee
from employee_app.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Employee
    """
    queryset = Employee.objects.filter(StatusBoolean=True)
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.StatusBoolean = False
            instance.save()
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)