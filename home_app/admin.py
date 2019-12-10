from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Home)

class Home(admin.ModelAdmin):
    fields = [("owner_first_name", "owner_last_name", "address_line_1", "postcode")]
