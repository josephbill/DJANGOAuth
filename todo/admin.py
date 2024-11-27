from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed")
    list_filter = ("title", "completed")
    search_fields = ("title", "user__username")
