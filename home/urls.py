from django.urls import path
from .views import home,resume_analysis

urlpatterns = [
  path("",home,name="home"),
  path('analyze/',resume_analysis,name='resume_analysis'),
]
