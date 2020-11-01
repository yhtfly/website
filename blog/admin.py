from django.contrib import admin
from . import models
# Register your models here.

class EntryAdmin(admin.ModelAdmin):

    list_display = ['title','author','visiting','create_time','modified']

admin.site.register(models.Category)
admin.site.register(models.Entry)
admin.site.register(models.Tag)