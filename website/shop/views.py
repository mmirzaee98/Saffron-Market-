from django.shortcuts import render
from shop.models import Product, Category

# This function renders the checkout page
def checkout(request):
    return render(request, 'checkout.html')

# This function renders a specific product's detail page
# The product is identified by its primary key (pk)
def product(request, pk):
    p = Product.objects.get(pk=pk)
    return render(request, 'product.html',{'product': p})

# This function renders the shop page, displaying all available products
def shop(request):
    category = request.GET.get('c')
    products = Product.objects.all()

    if category:
        category = Category.objects.get(id=category)
        products = products.filter(category=category)

    return render(request, 'shop.html', {'products': products,'category':category})
