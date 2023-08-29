from django.contrib import admin
from .models import POST

# Register your models here.
@admin.register(POST)

class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
    