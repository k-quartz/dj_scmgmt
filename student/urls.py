from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.index),
    path('display/',views.dispStudent),
    path('add/',views.createStudent),
    path('update/<str:id>',views.updateStudent),

    path('result/display/<str:id>',views.displayResult),
    path('result/add/<str:id>',views.createResult),
    path('result/update/<str:id>',views.UpdateResult),
]   