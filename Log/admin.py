from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models


# Register your models here.

class showLogs(admin.ModelAdmin):
    list_display = ["ip", "date", "time", "agent", "language"]


admin.site.register(models.Logger, showLogs)