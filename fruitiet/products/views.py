from django.shortcuts import render, Http404
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/home.html'
    return render(request, template, context)

def store(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/store.html'
    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all()
        context = {"product": product, "images": images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404
    
def search(request):
    try:
        query = request.GET.get('query')
    except:
        query = None
    if query:
        products = Product.objects.filter(title__icontains=query)
        context = {"query": query, "products": products}
        template = "products/results.html"
    else:
        template = "products/home.html"
        context = {}
    return render(request, template, context)
