from django.db import models

# Create category models here.
class Category(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



# Create Television category models here.
class TVCategory(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



# Create Computing models here.
class ComputingBrand(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name


# Create Property category models here.
class BedRoom(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



# Create Property category models here.
class BathRoom(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name


# Create division models here.
class Division(models.Model):
    name = models.CharField(max_length = 70, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'division')
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



#  Computing Generation
class ComputGeneration(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



# Create brand models here.
class Brand(models.Model):
    name = models.CharField(max_length = 70)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.name



# Create mobile models here.
class Mobile(models.Model):
    name = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    address = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 11)
    price = models.IntegerField()
    negotiable = models.BooleanField(default = False)
    description = models.TextField()
    image = models.ImageField(upload_to = 'products')
    condition_choice = (
        ('used','Used'),
        ('new','New'),
    )
    condition = models.CharField(max_length = 6, choices=condition_choice)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    division = models.ForeignKey(Division, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name



# Create television models here.
class Television(models.Model):
    name = models.CharField(max_length = 100)
    inches = models.IntegerField()
    address = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 11)
    price = models.IntegerField()
    negotiable = models.BooleanField(default = False)
    description = models.TextField()
    image = models.ImageField(upload_to = 'television')
    condition_choice = (
        ('used','Used'),
        ('new','New'),
    )
    condition = models.CharField(max_length = 6, choices=condition_choice)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    division = models.ForeignKey(Division, on_delete = models.CASCADE)
    brand = models.ForeignKey(TVCategory, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name



# Create Property models here.
class Property(models.Model):
    name = models.CharField(max_length = 100)
    square_feed = models.IntegerField()
    address = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 11)
    price = models.IntegerField()
    negotiable = models.BooleanField(default = False)
    description = models.TextField()
    image = models.ImageField(upload_to = 'property')
    condition_choice = (
        ('family','Family'),
        ('bachelor','Bachelor'),
    )
    condition = models.CharField(max_length = 10, choices=condition_choice)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    division = models.ForeignKey(Division, on_delete = models.CASCADE)
    bed_room = models.ForeignKey(BedRoom, on_delete = models.CASCADE)
    bath_room = models.ForeignKey(BathRoom, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name



# Create Education models here.
class Study (models.Model):

    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 11)
    pay_per_month = models.IntegerField()
    negotiable = models.BooleanField(default = False)
    description = models.TextField()
    image = models.ImageField(upload_to = 'study', blank = True, null = True)
    study_of_type = (
        ('bangla','Bangla'),
        ('english','English'),
        ('math','Math'),
        ('other','Others'),
    )
    study_type = models.CharField(max_length = 10, choices=study_of_type)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    division = models.ForeignKey(Division, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name




# Create mobile models here.
class Computing(models.Model):
    name = models.CharField(max_length = 100)
    model = models.ForeignKey(ComputGeneration, on_delete = models.CASCADE)
    address = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 11)
    price = models.IntegerField()
    negotiable = models.BooleanField(default = False)
    description = models.TextField()
    image = models.ImageField(upload_to = 'computing')
    condition_choice = (
        ('used','Used'),
        ('new','New'),
    )
    computing_types = (
        ('desktop','Desktop'),
        ('laptop','Laptop'),
        ('monitor','Monitor'),
        ('headphone','Headphone'),
        ('mouse','Mouse'),
        ('keyboard','Keyboard'),
    )
    condition = models.CharField(max_length = 6, choices=condition_choice)
    computing_type = models.CharField(max_length = 9, choices=computing_types)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    division = models.ForeignKey(Division, on_delete = models.CASCADE)
    brand = models.ForeignKey(ComputingBrand, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.name
