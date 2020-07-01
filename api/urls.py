from django.urls import path,include
from api import views

urlpatterns = [
    path('index/',views.index),
    path('',views.ListEmployee.as_view()),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
]