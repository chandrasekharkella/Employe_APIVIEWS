from django.urls import path
from empoloyeapi.views import EmployeeCreateApi, EmployeeApi, EmployeeUpdateApi, EmployeeDeleteApi,Employeelogin

urlpatterns = [
    path('api/get',EmployeeApi.as_view()),
    path('api/post',EmployeeCreateApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),
    path('api/login',Employeelogin.as_view()),
]
