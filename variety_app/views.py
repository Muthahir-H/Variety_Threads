from django.shortcuts import render
from admin_app.models import Product,Category
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    latest_products = Product.objects.order_by('-created_at')[:6]
    return render(request, 'index.html',{'latest_products':latest_products})

def products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 20)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj})


def contact(request):
    return render(request,'contact.html')
