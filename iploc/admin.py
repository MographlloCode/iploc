from django.contrib import admin
from .models import *

class IPs(admin.ModelAdmin):
    list_display = ('id','ip')
    list_display_links = ('id','ip')
    search_fields = ('ip',)
    list_per_page = 20


admin.site.register(IP, IPs)