from django.contrib import admin

from .models import Document, Folder, Topic

# Register your models here.
admin.site.register(Document)
admin.site.register(Folder)
admin.site.register(Topic)