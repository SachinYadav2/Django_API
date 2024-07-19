from . import views

from django.urls import path  , include
from rest_framework import routers

from api.views import CompnayViewSet , EmployeeViewSet


router = routers.DefaultRouter()


router.register(r'companies' , CompnayViewSet)

# Emplyee Router
router.register(r'emplyees' , EmployeeViewSet)

urlpatterns = [
    path("" , include(router.urls))
    # path()
]