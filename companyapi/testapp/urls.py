from django.urls import path
from . import views
app_name = "testapp"
urlpatterns = [
    path("page/" , views.home_page , name='page'),

]