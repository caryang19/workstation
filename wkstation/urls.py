from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('workstation/', views.workstation, name ='workstation'),
    path('export_csv/', views.export_csv, name ='export-csv'),
    
]