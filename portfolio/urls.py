from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.mainPage, name='main'),

   
    path('download/', views.download_file, name='download'),
  
]