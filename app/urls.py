from django.urls import path
from .views import home, associate_employee

urlpatterns = [
    path('', home, name='home'),
    path('associate_employee/<int:company_id>/', associate_employee, name='associate_employee'),
    
]