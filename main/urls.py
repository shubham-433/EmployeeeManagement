from django.urls import path
from .views import *
from main import views

# app_name = 'api'

urlpatterns = [
    path('', home, name='home'),
    path('add_employee/<int:company_id>/', add_employee, name='add_employee'),
    path('add_employee/new/', addNewEmployee, name='new_employee'),
    path('company/new/', addNewCompany, name='new_company'),
    
]