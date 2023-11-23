from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class AddressTable(models.Model):
    addressId = models.IntegerField(primary_key=True, auto_created=True)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    postcode = models.CharField(max_length=8)
    county = models.CharField(max_length=50)
    def __str__(self):
        return str(self.addressId)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, date_of_birth, sex, role, addressId, password='admin', **extra_fields):
        if not date_of_birth:
            raise ValueError('The Date of Birth field must be set')
        user = self.model(username=username, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, sex=sex, role=role, addressId=addressId, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password=password, **extra_fields)  # Remove the first_name and last_name arguments

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)
    role = models.CharField(max_length=30)
    addressId = models.IntegerField()  # You might want to use ForeignKey if the address is a separate model.

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'sex', 'role', 'addressId']

    class Meta:
        verbose_name = "User"

    def save(self, *args, **kwargs):
        # Set the password using the set_password method
        # This assumes that you have a field named 'password' in your model
        self.set_password(self.password)
        super().save(*args, **kwargs)

class Child(models.Model):
    childID = models.IntegerField(primary_key=True, auto_created=True)
    userID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    social_workerID = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='socialWorker')
    def __str__(self):
        return str(self.childID)

class Photos(models.Model):
    photoID = models.IntegerField(primary_key=True, auto_created=True)
    blob_link = models.CharField(max_length=50)
    photo_date = models.DateTimeField(default=timezone.now)
    child_photoID = models.ManyToManyField(Child)
    uploaderID = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, default=1, related_name='uploader')
    def __str__(self):
        return str(self.photoID)

class ChildrenHomes(models.Model):
    children_homeID = models.IntegerField(primary_key=True, auto_created=True)
    addressID = models.ForeignKey(AddressTable, on_delete=models.CASCADE)
    director = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, default=1, related_name='director')
    name = models.CharField(max_length=50, default='Home')
    def __str__(self):
        return str(self.childrenHomes)

class Staff(models.Model):
    staffID = models.IntegerField(primary_key=True, auto_created=True)
    childrenHomeID = models.ForeignKey(AddressTable, on_delete=models.CASCADE)
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.staffID)
    
class Journal(models.Model):
    entryID = models.IntegerField(primary_key=True, auto_created=True)
    entry = models.CharField(max_length=1000000)
    entry_date = models.DateTimeField()
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.entryID)