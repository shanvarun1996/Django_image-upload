from django.contrib import admin
from . models import ImageInfo
# Register your models here.

@admin.register(ImageInfo)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']