from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass
