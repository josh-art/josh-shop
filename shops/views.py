from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import User
from cart.views import Cart
from .forms import *
from .models import Contacts
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def contact(request):
    if request.method == "GET":
        return render(request, 'electrical.html')
    elif request.method== "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']
            contact = Contacts(user_name=name, email=email, mobile_number=mobile, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'electrical.html', {'success' : True})
        except Exception as e:
            print("error in request")
            return  render(request, 'electrical.html', {'success': False})

def feedback(request):
    return render(request, 'contact.html')


def AddVariation(request):
    name = 'Add Product Variation'
    form = VariationForm(request.POST or None, request.FILES or None)
    context = {
        'name': name,
        'form': form
    }
    if request.method == 'POST':
        form = VariationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Variation Saved')
            return redirect('AddVariation')
        else:
            messages.error(request, " Unsuccessfuly Adding Variation")
    else:
        return render(request, 'baseform.html', context)


@login_required(login_url='../../login/')
def AddFeatured(request):
    name = 'Add Featured Product '
    form = ProductFeaturedForm(request.POST or None)
    context = {
        'name': name,
        'form': form
    }
    if request.method == 'POST':
        form = ProductFeaturedForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Featured Product Saved')
            return redirect('AddFeatured')
        else:
            messages.error(request, " Unsuccessfuly Adding Featured Product")
    else:
        return render(request, 'baseform.html', context)




# Create your views here.
