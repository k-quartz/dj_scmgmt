from django.urls import path,include
from api import views

urlpatterns = [
    path('index/',views.index),
    path('',views.ListEmployee.as_view()),
    path('api/',include('djoser.urls')),
    path('api/',include('djoser.urls.authtoken')),
]