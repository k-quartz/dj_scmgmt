from rest_framework import serializers
from student import models

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields='__all__'

class StudentResultSerializes(serializers.ModelSerializer):
    class Meta:
        model=models.StudentResult
        fields='__all__'