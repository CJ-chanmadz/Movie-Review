from django.contrib import admin
from .models import Request

class display_to_admin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','movie_title')

# Register your models here.
admin.site.register(Request, display_to_admin)
