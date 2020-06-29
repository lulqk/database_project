from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'cars', views.CarViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]