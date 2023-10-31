from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(student)

class student(admin.ModelAdmin):
  list_display=['id','name','roll','address']