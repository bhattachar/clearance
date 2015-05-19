from django.db import models

# Create your models here.
from django.db import models




class Brand(models.Model):
	title = models.CharField(max_length=120)
	url = models.URLField()
	description = models.TextField(default=True, null=True)

	def __unicode__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=120)
	brand = models.CharField(max_length=120, blank=True, null=True)
	price = models.CharField(max_length=120)
	clearance = models.CharField(max_length=120)
	image = models.ImageField(upload_to='products/images/')
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	product_url = models.URLField(default="www.wowclearance.com")
	brand_url = models.URLField(default="www.wowclearance.com")
     

	def __unicode__(self):
		return self.title


# class Product(models.Model):
# 	title = models.CharField(max_length=120)
# 	brand = models.ForeignKey(Brand, null=True, related_name='Brand.title')
# 	price = models.CharField(max_length=120)
# 	clearance = models.CharField(max_length=120)
# 	image = models.ImageField(upload_to='products/images/')
# 	active = models.BooleanField(default=True)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	product_url = models.URLField(default="www.wowclearance.com")
# 	brand_url = models.ForeignKey(Brand, null=True, related_name='Brand.url')
     

# 	def __unicode__(self):
# 		return self.title