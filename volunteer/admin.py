from django.contrib import admin
from .models import Category, Country,State,City,Volunteer


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
# Register your models here.
admin.site.register(Category)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','category','mobile',)
admin.site.register(Volunteer,VolunteerAdmin)