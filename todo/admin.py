from django.contrib import admin
from .models import User, Task

# Register your models here.
admin.site.register([User, Task])