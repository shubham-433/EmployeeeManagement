from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Company, Employee
from .forms import *
from  django.views import View
from django.contrib import messages
def home(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})

def add_employee(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(request.POST['employee'])
        if form.is_valid():
            new_employ = Employee.objects.get(id=request.POST['employee'])
            new_employ.company = company
            new_employ.save()
            print(new_employ.company)
            messages.success(request, f"Employee {new_employ} Added to Company {new_employ.company} Successfully")
            return redirect('home')
        
    else:
        companies = Company.objects.all()
        form = EmployeeForm()
        employees = company.employee_set.all()
        return render(request, 'add_employee.html', {'company': company, 'form': form, 'employees': employees,"companies":companies})

# def home(request):
#     companies = Company.objects.all()
#     # company = Company.objects.get(id=id)
#     # print(company)
#     form = EmployeeForm()
#     # employees = company.employee_set.all()
#     return render(request, 'companies.html', {'companies': companies,'form':form})

def addNewEmployee(request):
    if request.method== 'POST':
           form = NewEmployeeForm(request.POST)
           print(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request,f"{request.POST['first_name']} {request.POST['last_name']} add succesfully")
            #    messages.success(request,f"{request.}")
           return HttpResponseRedirect('/add_employee/new/')
    
    else:
        form=NewEmployeeForm()
        return render(request,'newEmployeeForm.html',{'form':form})
        

def addNewCompany(request):
    if request.method== 'POST':
           form = NewCompnayForm(request.POST)
           print(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request,f" Company {request.POST['name']} created succesfully")
           return HttpResponseRedirect('/company/new/')
    
    else:
        form=NewCompnayForm()
        return render(request,'newCompanyForm.html',{'form':form})