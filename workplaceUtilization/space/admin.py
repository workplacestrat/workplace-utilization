from django.contrib import admin

# Register your models here.

from .models import Study, Space, dayRecord, spaceRecord

admin.site.register(Study)
admin.site.register(Space)
admin.site.register(dayRecord)
admin.site.register(spaceRecord)
