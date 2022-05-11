from django.db import models


# Create your models here.
# used to populate the database. Each class represents a table or a document in the database

class RoomType(models.Model):
    R_type = models.CharField(max_length=150, primary_key=True)

    def __str__(self):
        return self.R_type

class Landlord(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.first_name+' '+self.last_name
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=50, help_text='Area Located in Town')
    house_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='hostelT')
    ratings = models.IntegerField()
    verified = models.BooleanField(default=False)
    image_url = models.URLField()
    image_url1 = models.URLField(null=True, default='')
    image_url2 = models.URLField(null=True, default='')
    price = models.PositiveIntegerField()
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='lords')
    agent = models.CharField(max_length=30, default='')
    town = models.CharField(max_length=50, help_text="The town where the property is located")
    availability = models.BooleanField(default=True)
    units_available = models.IntegerField(null=False)
    features = models.CharField(max_length=500, default='')
    requirement = models.CharField(max_length=750, default='')


    class Meta:
        ordering = ['units_available']

    def __str__(self):
        return self.name+" \t\t "+self.location

    def available(self):
        if self.units_available == 0:
            self.available = False
        else:
            self.available = True


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=100)
    house = models.ForeignKey(Listing, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.id+"  "+self.room_type

class ConfirmedBookings(models.Model):
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.DateTimeField()
    Amount_paid = models.IntegerField()
    payment_code = models.CharField(max_length=100)

    def __str__(self):
        return self.id+"  "+self.booking+"   "+self.Amount_paid
