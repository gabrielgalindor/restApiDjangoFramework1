from django.urls import path
from restapidjango import views

urlpatterns = [
    path('hello/', views.HelloApi.as_view()),
    path('test/', views.pruebaAuth.as_view())
]
