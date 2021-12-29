from django.contrib import admin
from .models import Contact,Project,DigitalNote
# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(DigitalNote)