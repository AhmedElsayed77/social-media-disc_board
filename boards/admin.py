from django.contrib import admin
from .models import Board, Topic
from import_export.admin import ImportExportModelAdmin  
admin.site.register(Board) 
@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    pass