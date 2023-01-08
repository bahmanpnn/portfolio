from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Langueges)
admin.site.register(models.Contact)
admin.site.register(models.Skills)
admin.site.register(models.Clients)
admin.site.register(models.Degrees)
admin.site.register(models.Experiences)
admin.site.register(models.Portfolio)
admin.site.register(models.Services)
