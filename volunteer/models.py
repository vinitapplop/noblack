from django.db import models
# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=300)
    country_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country = models.ForeignKey(Country, related_name='states')
    state_name = models.CharField(max_length=300)
    state_code = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ForeignKey(State, related_name='cities')
    city_name = models.CharField(max_length=300)
    city_code = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.city_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Volunteer(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, null=True)
    volunteering_for = models.TextField(max_length=10000, blank=True, null=True)
    city = models.ForeignKey(City, null=True)
    landmark = models.CharField(max_length=200,null=True,blank=True)
    otp = models.CharField(max_length=10, blank=True, null=True)
    mobile_verified = models.BooleanField(default=False)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    avaiable_from = models.TimeField(null=True,blank=True)
    avaiable_till = models.TimeField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def isComplete(self):
        if(self.first_name == None or len(self.first_name) ==0):
            return False
        if (self.last_name == None or len(self.last_name) == 0):
            return False