from rest_framework import serializers
from api import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Employee
        fields='__all__'


