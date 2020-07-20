from django.contrib import admin

# Register your models here.

from .models import *

#register to admin page
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)