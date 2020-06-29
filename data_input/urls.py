from django.urls import path
from . import views

app_name = 'data_input'

urlpatterns = [
    path('', views.index, name='index'),
    path('export/<int:id>/', views.export_to_mongo, name='export'),
]