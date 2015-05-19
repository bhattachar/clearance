import json
import urllib2
from products.models import Product


url = "https://api.import.io/store/data/2a2f0b4f-6f38-4b88-a23e-c3e70876b107/_query?input/webpage/url=http%3A%2F%2Fwww.cleo.ca%2Fsale%2Fshop-clearance%2F&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj = urllib2.urlopen(url)
data = json.load(obj)
for i in data['results']:
	Product.objects.get_or_create(title=i['title'], price=i['price'], clearance=i['clearance'], image=i['image'], product_url=i['title_link'], brand='Cleo', brand_url='http://www.cleo.ca/sale/shop-clearance/')