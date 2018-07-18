from rest_framework import serializers
from employee_app.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    Status = serializers.SerializerMethodField('status_conversion')

    class Meta:
        model = Employee
        fields = ('id', 'FirstName', 'MiddleInitial','LastName','DateOfBirth','DateOfEmployment', 'Status')

    def status_conversion(self, obj):
        if obj.StatusBoolean:
            return "ACTIVE"
        return "INACTIVE"
