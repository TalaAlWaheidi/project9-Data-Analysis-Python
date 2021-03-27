from django.db import models

# Create your models here.

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  


class Person(models.Model):
    Data_source = models.CharField(max_length=80,null=True)
    Project_Number = models.CharField(max_length=80)
    Legacy_Project_Number = models.CharField(max_length=80)
    City = models.CharField(max_length=80)
    Country = models.CharField(max_length=80)
    Zip_Code = models.CharField(max_length=80)
    Sector = models.CharField(max_length=80)
    Electric_Utility = models.CharField(max_length=80)
    Purchase_Type = models.CharField(max_length=80)
    Date_Application_Received = models.CharField(max_length=80)
    Date_Completed = models.CharField(max_length=80)
    Project_Status = models.CharField(max_length=80)
    Contractor = models.CharField(max_length=80)
    Primary_Inverter_Manufacturer = models.CharField(max_length=80)
    Primary_Inverter_Model_Number = models.CharField(max_length=80)
    Total_PV_Module_Quantity = models.CharField(max_length=80)
    Total_Inverter_Quantity = models.CharField(max_length=80)
    Primary_PV_Module_Manufacturer = models.CharField(max_length=80)
    PV_Module_Model_Number = models.CharField(max_length=80)
    Project_Cost = models.CharField(max_length=80)
    Incentive = models.CharField(max_length=80)
    Total_Nameplate_kW_DC = models.CharField(max_length=80)
    Expected_KWh_Annual_Production = models.CharField(max_length=80)
    Georeference = models.CharField(max_length=80)
   
    


# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     #birth_date = models.DateField()
#     location = models.CharField(max_length=100, blank=True)
    
