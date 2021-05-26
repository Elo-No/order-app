from django.contrib import admin
from .models import *

# admin.site.register(Customers)
# admin.site.register(Items)


# # Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['Name',
                    'Family',
                    'Address',
                    'Zip_Code',
                    'Phone',
                    'Phone_Whats_App',
                    'Pic',
                    'Size_Of_Product',
                    'Description',
                    'Debt_Rate',
                    'Type_Of_Product']


admin.site.register(Customers, CustomersAdmin)
