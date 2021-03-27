from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person
from .models import Employee

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = (
    'Data_source', 
    'Project_Number', 
    'Legacy_Project_Number', 
    'City',
    'Country',
    'Zip_Code',
    'Sector',
    'Electric_Utility',
    'Purchase_Type',
    'Date_Application_Received',
    'Date_Completed',
    'Project_Status',
    'Contractor',
    'Primary_Inverter_Manufacturer',
    'Primary_Inverter_Model_Number',
    'Total_PV_Module_Quantity',
    'Total_Inverter_Quantity',
    'Primary_PV_Module_Manufacturer',
    'PV_Module_Model_Number',
    'Project_Cost',
    'Incentive',
    'Total_Nameplate_kW_DC',
    'Expected_KWh_Annual_Production',
    'Georeference',
    )

@admin.register(Employee)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('eid', 'ename', 'eemail','econtact')