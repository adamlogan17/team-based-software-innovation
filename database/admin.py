from .models import *
from django.contrib import admin
from django.utils.safestring import *
from mysite.admin import customAdminSite
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin

# Import your custom user model
from .models import CustomUser

# Register your custom user model
admin.site.register(CustomUser)

# Ensure that LogEntry is using your custom user model
LogEntry._meta.get_field('user').remote_field.model = CustomUser

@admin.register(AddressTable)
class AddressTableAdmin(admin.ModelAdmin):
    list_display = ('addressId', 'addressLine1', 'addressLine2', 'postcode', 'county')
    search_fields = ('addressId', 'addressLine1', 'addressLine2', 'postcode', 'county')

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'date_of_birth', 'sex', 'role', 'addressId', 'is_active', 'is_staff')
#     search_fields = ('username', 'first_name', 'last_name', 'addressId__addressLine1', 'addressId__addressLine2')
#     list_filter = ('is_active', 'is_staff', 'date_of_birth', 'sex', 'role')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('childID', 'userID', 'socialWorker')
    search_fields = ('childID', 'userID__username', 'socialWorker__username')
    list_filter = ('userID__role', 'socialWorker__role')

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('photoID', 'blobLink', 'photoDate')
    search_fields = ('photoID', 'blobLink')
    list_filter = ('photoDate',)

@admin.register(ChildrenHomes)
class ChildrenHomesAdmin(admin.ModelAdmin):
    list_display = ('childrenHomes', 'addressID')
    search_fields = ('childrenHomes', 'addressID__addressLine1', 'addressID__addressLine2', 'addressID__postcode')
    list_filter = ('addressID__county',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffID', 'childrenHomeID', 'userID')
    search_fields = ('staffID', 'childrenHomeID__addressLine1', 'childrenHomeID__addressLine2', 'childrenHomeID__postcode', 'userID__username')
    list_filter = ('childrenHomeID__county', 'userID__role')


for model, admin_class in admin.site._registry.items():
    customAdminSite.register(model, admin_class.__class__)

customAdminSite.index_template = 'admin/extendedAdminPage.html'  # Path to custom template for admin index page
admin.site.index_template = 'admin/extendedAdminPage.html'  # Path to custom template for admin index page