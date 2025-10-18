
from django.contrib import admin
from django.urls import path
from Practical_App2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('add_salepage/', add_salepage, name="add_salepage"),
    path('salesData/', salesData, name="salesData"),
]
