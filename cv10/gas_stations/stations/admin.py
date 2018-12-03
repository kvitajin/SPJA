from django.contrib import admin

# Register your models here.
from django.contrib import admin
from stations.models import Station, Company

admin.site.register(Company)
admin.site.register(Station)
