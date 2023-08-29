from django.contrib import admin

# Register your models here.
from .models import Producs , Profile , Category

admin.site.register(Producs)
admin.site.register(Profile)
admin.site.register(Category)