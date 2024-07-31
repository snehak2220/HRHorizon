from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from .models import Employee_Details
# Create your views here.
def index(request):
    return render(request,"new_index.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if not username or not password:
            messages.error(request,'fields are empty')
            return render(request,'signup.html')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return render(request, "signup.html")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/signin')
        else:
            messages.error(request, "password does not match")
            return render(request, 'signup.html')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'home1.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')
    return render(request, 'signin.html')


def add(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname = request.POST['lname']
        age = request.POST['age']
        designation = request.POST['desig']
        salary = request.POST['salary']

        employee=Employee_Details(
            First_Name=firstname,
            Last_Name=lastname,
            Age=age,
            Designation=designation,
            Salary=salary
        )
        employee.save()
        return redirect('/view_employee')

    return render(request,'add_employee.html')
def view(request):
    emp_list=Employee_Details.objects.all()
    return render(request,'details.html',{'emp_list':emp_list})

def update(request,emp_id):
    emp=Employee_Details.objects.get(id=emp_id)
    if request.method=='POST':
        emp.First_Name = request.POST['fname']
        emp.Last_Name = request.POST['lname']
        emp.Age = request.POST['age']
        emp.Designation = request.POST['desig']
        emp.Salary = request.POST['salary']
        emp.save()
        return redirect('/view_employee')
    return render(request,'update.html',{'emp':emp})
def delete(request,emp_id):
    emp = Employee_Details.objects.get(id=emp_id)
    emp.delete()
    return redirect('/view_employee')

def logout(request):
    auth.logout(request)
    return redirect('/')
def home(request):
    return render(request,'home1.html')