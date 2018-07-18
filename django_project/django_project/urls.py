from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from employee_app.views import EmployeeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
