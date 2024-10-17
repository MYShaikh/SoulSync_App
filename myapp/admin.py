from django.contrib import admin
from .models import Books, Ouruser, Product, RegisteredUsers
# Register your models here.
admin.site.register(Books)
admin.site.register(Ouruser)
admin.site.register(Product)
admin.site.register(RegisteredUsers)