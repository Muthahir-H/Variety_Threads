from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm,CategoryForm
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.shortcuts import redirect


def admin_index(request):
    return render(request,'admin/admin_home.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Successfully Added')
            return redirect('product_list') 
    else:
        form = ProductForm()
        messages.error(request,'Something Went Wrong')
    return render(request, 'admin/add_product.html', {'form': form})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Successfully Updated')
            return redirect('product_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)

    return render(request, 'admin/update_product.html', {'form': form, 'product': product})

def admin_delete_movie(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product Successfully Deleted")
        return redirect("product_list")
    
    return render(request, "admin/admin_confirm_delete.html", {"product": product})


def product_list(request):
    product_list = Product.objects.all().order_by('id')
    paginator = Paginator(product_list, 16)  # Show 6 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/product_list.html', {'page_obj': page_obj})


def createcategories(request):
    if request.POST:
        form=CategoryForm(request.POST)

        if form.is_valid():
            category=form.save(commit=False)
            category.save()
            messages.success(request,'Category Successfully Created')
            return redirect('add_category')
        else:
            messages.error(request,'Something Went Wrong')
    else:
        form=CategoryForm()

    categories=Category.objects.all()

    return render(request,'admin/add_category.html',{'form':form,'categories':categories})


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.success(request, 'Category has been deleted successfully.')
    return redirect('add_category')

def logout_view(request):
    logout(request)
    return redirect('index')