
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import NC
from django.http import  HttpResponse
import csv
from import_export.admin import ImportExportModelAdmin
from .forms import NCForm
from .models import NC

admin.site.site_header = 'Não conformidades ESCH'
class NCAdmin(ImportExportModelAdmin):
    list_display = ('Municipio','TN','Descricao','Unidade','Prazo','Situacao','OBS')
    list_filter = ('Municipio','TN','Descricao','Unidade','Prazo','Situacao','OBS')




admin.site.register(NC,NCAdmin)



admin.site.unregister(Group)


