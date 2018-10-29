from django.contrib import admin

from .models import Continent, Country, Location

# Register your model

class ContinetAdmin(admin.ModelAdmin):
    list_display= ["name"]

class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "continent"]

class LocationAdmin(admin.ModelAdmin):
    list_display= ["continent", "country", "area", "city", "street"]

admin.site.register(Continent, ContinetAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Location, LocationAdmin)

