from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'products.html')

def productDetail(request):
    return render (request, 'product_detail.html')
