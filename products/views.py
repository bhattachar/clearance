from django.shortcuts import render
from .models import Product, Brand




	
# front end template rendering function start

def home(request):

	products = Product.objects.order_by("-clearance")
	brands = Brand.objects.all()
	context = {'products': products, 'brands': brands}

	template = "home.html"
	return render(request, template, context)

# front end template rendering function end





def search(request):

	
	try:
		q = request.GET.get('q', '')
	except:
		q = False
	if q:
		query = "You searched for: %s" %(q)
		k = q.split()
		if len(k) > 2:
			products = []
			for item in k:
				all_products = Product.objects.filter(title__icontains=item).distinct()
				for product in all_products:
					if product not in products:
						products.append(product)
		else:
			products = Product.objects.filter(title__icontains=q)	

    
	context = locals()
	template = "results.html"
					
	return render(request, template, context)


# product search function end                                                                                          