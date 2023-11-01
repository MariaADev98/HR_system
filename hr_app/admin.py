from django.contrib import admin
from .models import Tasks




@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'time_update')


# Register your models here.
