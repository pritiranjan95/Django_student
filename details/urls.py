from django.contrib import admin
from django.urls import path,include
from details import views

urlpatterns = [
    path('student/<int:pk>',views.Studentdata.as_view()),
    path('student',views.Studentdata.as_view())
]