from django.contrib import admin
from .models import Product, Brand
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display = ["title", "brand", "price", "clearance", "active", "timestamp", "updated"]
	list_editable = ["title", "price", "clearance", "active", "brand"]
	search_fields = ["title"]
	
	class Meta:
		model=Product



admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)