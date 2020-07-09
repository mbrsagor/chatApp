from django.db import models
from django.contrib.auth.models import User


# Create Serivce models here.
class Service(models.Model):
    name = models.CharField(max_length = 70)
    service_ulr = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'services')
    create_at = models.DateTimeField(auto_now_add = False, auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.name



# Create Serivce models here.
class Team(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 30)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'team')
    create_at = models.DateTimeField(auto_now_add = False, auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.name




# Create Pricing Table models here.
class Pricing(models.Model):
    plane_name = models.CharField(max_length = 20)
    price = models.IntegerField()
    colum1 = models.CharField(max_length = 35)
    colum2 = models.CharField(max_length = 35)
    colum3 = models.CharField(max_length = 35, blank = True, null = True)
    colum4 = models.CharField(max_length = 35, blank = True, null = True)
    colum5 = models.CharField(max_length = 35, blank = True, null = True)

    def __str__(self):
        return self.plane_name



# Create Customar-Review models here.
class Review(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 30)
    comments = models.TextField()
    image = models.ImageField(upload_to = 'customar-review')

    def __str__(self):
        return self.name



# Create User Profile Setting models here.
class UpdateProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    SELECT_GENDER =(
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length = 8, choices=SELECT_GENDER)
    address = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 60)
    phone_number = models.IntegerField(unique=True)
    user_bio = models.TextField()
    image = models.ImageField(upload_to = 'profile_setting', blank = True, null = True)

    def __str__(self):
        return self.full_name
