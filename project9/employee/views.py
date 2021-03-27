from django.shortcuts import render, redirect  
# from employee.forms import EmployeeForm  
from employee.models import Employee  
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from .models import Person
from .forms import EmployeeForm
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

import time
from humanfriendly import format_timespan

import sqlite3 

import mysql.connector

import re



# Create your views here. 
def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            return redirect ('/admin/read')

    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})







##################################################################################

def emp(request):  
    if request.method == "POST":  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/admin/read')  
            except:  
                pass  
    else:  
        form = SignupForm()
    return render(request,'admin-create.html',{'form':form})  
def show(request):  
    employees = User.objects.all()   
    return render(request,"admin-read.html",{'employees':employees})  
def edit(request, id):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')  
    employee = User.objects.get(id=id)  
    return render(request,'admin-update.html', {'employee':employee})  
def update(request, id):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')  
    employee = User.objects.get(id=id)  
    form = SignupForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()
        return redirect("/admin/read")
    else:
     messages.success(request,'Your Account')  
    return render(request, 'admin-update.html', {'employee': employee})  
def destroy(request, id):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')  
    employee = User.objects.get(id=id)
    employee.delete()  
    messages.success(request,'Your Account') 
    return redirect("/admin/read")

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def simple_upload(request):
    begin_time = time.time()
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    if request.method == 'POST':
        
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        
        if str(new_persons).endswith('.xlsx'):
            imported_data = dataset.load(new_persons.read(),format='xlsx')
        else:
            imported_data = dataset.load(new_persons.read().decode('UTF-8'))

        
        data_source = request.POST['Data_source']
      

        #print(imported_data)
        for data in imported_data:
        	# print(data[1])
        	value = Person(
                Data_source=data_source,
        		Project_Number=data[0],
        		Legacy_Project_Number=data[1],
        		City=data[2],
        		Country=data[3],
        		Zip_Code=data[4],
        		Sector=data[5],
        		Electric_Utility=data[6],
        		Purchase_Type=data[7],
        		Date_Application_Received=data[8],
        		Date_Completed=data[9],
        		Project_Status=data[10],
        		Contractor=data[11],
        		Primary_Inverter_Manufacturer=data[12],
        		Primary_Inverter_Model_Number=data[13],
        		Total_PV_Module_Quantity=data[14],
        		Total_Inverter_Quantity=data[15],
        		Primary_PV_Module_Manufacturer=data[16],
        		PV_Module_Model_Number=data[17],
        		Project_Cost=data[18],
        		Incentive=data[19],
        		Total_Nameplate_kW_DC=data[20],
        		Expected_KWh_Annual_Production=data[21],
        		Georeference=data[22],
        	    )
        	value.save()
    
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
    
        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
   
    end_time = time.time() - begin_time
    result = format_timespan(end_time)
   
    Persons = Person.objects.all() 
    return render(request, 'excel-uploads.html',{'persons': Persons,'result':result})



# def admin(request):

#     # return render(request,'app/welcome.html')
#          return render(request, 'app/Admin/signin.html')
#     else :
#         return render(request, 'app/Admin/index.html')
# import required modules

# connect python with mysql with your hostname, 



def dashboardPage(request):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    else:
        my_connect = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="djangodb"
                )
        ####### end of connection ####
        my_cursor = my_connect.cursor()
        my_cursor.execute("SELECT COUNT(*) from employee_person where Contractor='Complete'")
        res = my_cursor.fetchone()
        for num in res:
            val = num

        my_cursor2 = my_connect.cursor()
        my_cursor2.execute("SELECT COUNT(*) from employee_person where Contractor='Pipeline'")
        res2 = my_cursor2.fetchone()
        for num2 in res2:
            val2 = num2

        my_cursor3 = my_connect.cursor()
        my_cursor3.execute("SELECT SUM(Total_Inverter_Quantity) FROM employee_person WHERE Primary_Inverter_Manufacturer='Solar Works, Inc.'")
        res3 = my_cursor3.fetchone()
        for num3 in res3:
            Solar_Works_Inc = num3

        my_cursor4 = my_connect.cursor()
        my_cursor4.execute("SELECT SUM(Total_Inverter_Quantity) FROM employee_person WHERE Primary_Inverter_Manufacturer='SunRun Inc.'")
        res4 = my_cursor4.fetchone()
        for num4 in res4:
            SunRun_Inc = num4

        my_cursor5 = my_connect.cursor()
        my_cursor5.execute("SELECT SUM(Total_Inverter_Quantity) FROM employee_person WHERE Primary_Inverter_Manufacturer='SunPower Capital LLC'")
        res5 = my_cursor5.fetchone()
        for num5 in res5:
            SunPower = num5

        my_cursor6 = my_connect.cursor()
        my_cursor6.execute("SELECT SUM(Total_Inverter_Quantity) FROM employee_person WHERE Primary_Inverter_Manufacturer='VIVINT SOLAR'")
        res6 = my_cursor6.fetchone()
        for num6 in res6:
            Vivint = num6
                    
        return render(request, 'dashboard.html',{'complete':val,'notcomplete':val2,'Solar_Works_Inc':Solar_Works_Inc,'SunRun_Inc':SunRun_Inc,'SunPower':SunPower,'Vivint':Vivint})
def adminCreatePage(request):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    return render(request, 'admin-create.html')
def adminReadPage(request):
    return render(request, 'admin-read.html')
def adminUpdatePage(request):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    else:
        return render(request, 'admin-update.html')
# def adminDeletePage(request):
#     return render(request, 'admin-delete.html')
def excelUploadsPage(request):
        if not request.user.is_authenticated:
            return render(request,'registration/login.html')
        else:
            return render(request, 'excel-uploads.html')