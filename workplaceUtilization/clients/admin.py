from django.contrib import admin

# Register your models here.

from .models import Client, Project, Building

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Building)
