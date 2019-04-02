from django.contrib import admin
from .models import Todo

print(Todo)

# Register your models here.
admin.site.register(Todo)