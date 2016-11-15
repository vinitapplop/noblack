from django.contrib import admin
from .models import Category, Country,State,City,Volunteer


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
# Register your models here.
admin.site.register(Category)
admin.site.register(Volunteer)