from django.shortcuts import get_object_or_404, render, redirect
from empmngt.models import Calender, Employee, News, Job
from empmngt.forms import CalenderForm, EmployeeForm, NewsForm, JobForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

def home(request):
    return render(request, 'empmngt/home.html')

@login_required
def addnews(request):
    f=NewsForm()
    if request.method == 'POST':
        f = NewsForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "News Added Successfully!" )
            return redirect('/news')
    return render(request, 'empmngt/addnews.html',  {'form':f})

@login_required
def calender(request):
    f=CalenderForm()
    if request.method == 'POST':
        f = CalenderForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Holiday was added successfully.')
            return redirect('/holidays')
    return render(request, 'empmngt/calender.html',  {'form':f})

@login_required
def viewemp(request):
    data = Employee.objects.all()
    return render(request, 'empmngt/viewemp.html', {'d': data})

def holidays(request):
    data = Calender.objects.all()
    return render(request, 'empmngt/holidays.html', {'d': data})

def news(request):
    data = News.objects.last()
    return render(request, 'empmngt/news.html', {'d': data})


@login_required
def employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            employee_obj = form.save()

            messages.success(
                request,
                f"Employee {employee_obj.Emp_ID} added successfully."
            )

            return redirect("viewemp")

    else:
        form = EmployeeForm()

    return render(
        request,
        "empmngt/addemp.html",
        {"form": form}
    )



@login_required
@never_cache
def dashboardview(request):
    return render(request, 'empmngt/dashboard.html')

def empdashboard(request):
    return render(request, 'empmngt/empdash.html')


def loginview(request):
    
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")

            # Change this URL to your actual dashboard URL.
            return redirect("hrmanager")

        else:
            messages.error(
                request,
                "Invalid username or password. Please try again."
            )

    return render(request, "registration/login.html")


def logoutview(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

@login_required
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="employeelist.csv"'
    employee = Employee.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Name', 'Emp ID', 'Designation','Department', 'Annual CTC', 'Experience'])
    for emp in employee:
        writer.writerow([emp.Name, emp.Emp_ID, emp.Designation, emp.Department, emp.Annual_CTC, emp.Experience])
    return response


@login_required
def employee_detail(request, id):
    data = Employee.objects.get(id=id)

    skills_list = [
        skill.strip()
        for skill in data.Skills.split(",")
        if skill.strip()
        ]
    return render(
        request,
        "empmngt/empprofile.html",
        {"d": data, "skills_list": skills_list}
    )

@login_required
def updateview(request, id):
    data = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Employee profile updated successfully!"
            )
            return redirect("viewemp")

    else:
        form = EmployeeForm(instance=data)

    return render(
        request,
        "empmngt/empupdate.html",
        {"d": data, "form": form}
    )


@login_required
def newsupdate(request, id):
    data = News.objects.get(id=id)
    if request.method == 'POST':
        f = NewsForm(request.POST, instance=data)
        if f.is_valid():
            data = f.save(commit=False)
            data.is_edited = True
            data.save()
            messages.success(
                request,
                "News updated successfully!"
            )
            return redirect('/news')
    else:
        f = NewsForm(instance=data)
    return render(request, 'empmngt/newsupdate.html', {'d': data, 'form': f})


@login_required
def newsdelete(request, id):
    data = News.objects.get(id=id)
    data.delete()
    messages.success(request, "News deleted successfully.")
    return redirect('/news/')

@login_required
def deleteview(request, id):
    data = Employee.objects.get(id=id)
    data.delete()    
    messages.success(request, "Employee deleted successfully.")
    return redirect('/viewemp')

@login_required
def deleteholiday(request, id):
    data = Calender.objects.get(id=id)
    data.delete()    
    messages.success(request, "Calender deleted successfully.")
    return redirect('/holidays')

@login_required
def holidayupdate(request, id):
    data = Calender.objects.get(id=id)
    if request.method == 'POST':
        f = CalenderForm(request.POST, instance=data)
        if f.is_valid():
            data = f.save(commit=False)
            data.is_edited = True
            data.save()
            messages.success(request, "Holiday updated successfully.")
            return redirect('/holidays')
    else:
        f = CalenderForm(instance=data)
    return render(request, 'empmngt/holidayupdate.html', {'d': data, 'form': f})

@login_required
def jobopen(request):
    f=JobForm()
    if request.method == 'POST':
        f = JobForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "Job opening added successfully.")
            return redirect('/jobs')
    return render(request, 'empmngt/jobopen.html',  {'form':f})

def jobs(request):
    data = Job.objects.all()
    return render(request, 'empmngt/jobs.html', {'d': data})

@login_required
def jobupdate(request, id):
    data = Job.objects.get(id=id)
    if request.method == 'POST':
        data.Role = request.POST['Role']
        data.Experience = request.POST['Experience']
        data.Skills = request.POST['Skills']
        data.CTC = request.POST['CTC']
        data.Notice_Period = request.POST['Notice_Period']
        data.save()
        messages.success(request, "Job Updated successfully.")
        return redirect('/jobs/')

    return render(request, 'empmngt/jobupdate.html', {'d': data})

@login_required
def jobdelete(request, id):
    data = Job.objects.get(id=id)
    data.delete()
    messages.success(request, "Job deleted successfully.")    
    return redirect('/jobs/')

