from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.index),
    path('add/',views.createStudent),
    path('display/',views.dispStudent),
    path('update/<str:id>',views.updateStudent),
]   