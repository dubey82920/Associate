

# Create your views here.
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import Company, Employee

def home(request):
    companies = Company.objects.all()
    employees = Employee.objects.all()
    context = {
        'companies': companies,
        'employees': employees
    }
    return render(request, 'home.html', context)

def associate_employee(request, company_id):
    company = Company.objects.get(id=company_id)
    employees = Employee.objects.filter(company=company)
    if request.method == 'POST':
        try:
            employee_id = request.POST['employee']
            employee = Employee.objects.get(id=employee_id)
            employee.company = company
            employee.save()
            return redirect('home')
        except MultiValueDictKeyError:
            # handle case where 'employee' key is not present in POST data
            pass
    context = {
        'company': company,
        'employees': employees
    }
    return render(request, 'associate_employee.html', context)