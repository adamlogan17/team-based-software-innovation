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
    list_display = ('addressId', 'address_line1', 'address_line2', 'postcode', 'county')
    search_fields = ('addressId', 'address_line1', 'address_line2', 'postcode', 'county')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('childID', 'userID', 'social_workerID')
    search_fields = ('childID',)

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('photoID', 'blob_link', 'photo_date', 'uploaderID')
    search_fields = ('photoID', 'blob_link')
    list_filter = ('photo_date',)

@admin.register(ChildrenHomes)
class ChildrenHomesAdmin(admin.ModelAdmin):
    list_display = ('children_homeID', 'addressID', 'director', 'name')
    search_fields = ('children_homeID', 'addressID__addressLine1', 'addressID__addressLine2', 'addressID__postcode')
    list_filter = ('addressID__county',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffID', 'childrenHomeID', 'userID')
    search_fields = ('staffID', 'childrenHomeID__addressLine1', 'childrenHomeID__addressLine2', 'childrenHomeID__postcode', 'userID__username')
    list_filter = ('childrenHomeID__county', 'userID__role')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('entryID', 'entry', 'entry_date', 'userID')
    search_fields = ('entryID', 'entry_date')
    list_filter = ('userID', 'entry_date')

for model, admin_class in admin.site._registry.items():
    customAdminSite.register(model, admin_class.__class__)

customAdminSite.index_template = 'admin/extendedAdminPage.html'  # Path to custom template for admin index page
admin.site.index_template = 'admin/extendedAdminPage.html'  # Path to custom template for admin index page