from django.urls import path,include # type: ignore
from Api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers # type: ignore
# Setting App-level urls using routers 
# typically use them to avoid manually writing multiple URL patterns for different HTTP methods (GET, POST, PUT, DELETE, 

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls)),
]