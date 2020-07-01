from django.shortcuts import render
from student import serializers
from student import models
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BasicAuthentication, SessionAuthentication




# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,])
def dispStudent(request):

    student=models.Student.objects.all()
    serializer=serializers.StudentSerializers(student,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,])
def createStudent(request):
    stu_serializer=serializers.StudentSerializers(data=request.data)
    stu_serializer.is_valid(raise_exception=True)
    stu_serializer.save()
    return Response(stu_serializer.data,status=201)


@api_view(['POST'])
#@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,])
def updateStudent(request,id):
    
    snippet=models.Student.objects.get(id=id)
    stu_serializer=serializers.StudentSerializers(instance=snippet,data=request.data)

    if stu_serializer.is_valid():
        stu_serializer.save()
        return Response(stu_serializer.data,status=201)
    else:
        return Response(stu_serializer.errors,status=400)

@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,])
def displayResult(request,id):
    result=models.StudentResult.objects.filter(student_id=id)
    serializer=serializers.StudentResultSerializes(result,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,])
def createResult(request,id):
    serializer=serializers.StudentResultSerializes(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

@api_view(['POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,])
def UpdateResult(request,id):
    snippet=models.StudentResult.objects.get(id=id)

    serializer=serializers.StudentResultSerializes(instance=snippet,data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)


def index(request):
    return render(request,"student/index.html")
    




