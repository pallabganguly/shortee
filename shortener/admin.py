from django.contrib import admin

# Register your models here.
from .models import UrlShort    # class-name of app model

admin.site.register(UrlShort)
