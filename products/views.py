from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from account.models import Profils
from account.forms import UserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    products = Product.objects.order_by("-created_at")[:3]
    return render(request, "home.html", {"products": products})


@login_required
def profile(requesr):
    return render(requesr, "profile.html", {})


@login_required
@permission_required("products.add_product")
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if Product.objects.filter(name__iexact=name, owner=request.user).exists():
                form.add_error("name", "هذا المنتج موجود لديك مسبقاً")
        else:
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("products")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})


@login_required
@permission_required("products.view_product")
def my_products(requesr):
    products = Product.objects.filter(owner=requesr.user)
    return render(requesr, "my_products.html", {"products": products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_detail.html", {"product": product})


@login_required
@permission_required("products.change_product")
def edit_product(request, id):
    product = get_object_or_404(Product, id=id, owner=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("my_products")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"product": product, "form": form})


def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request, "products.html", {"products": products})


def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": products})


def search(request):
    search = request.GET.get("search")
    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    products = Product.objects.all()
    if search:
        products = products.filter(name__icontains=search)
    if category:
        products = products.filter(category=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    return render(request, "products.html", {"products": products})


@login_required
@permission_required("products.delete_product")
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, owner=request.user)
    if request.method == "POST":
        product.delete()
        return redirect("my_products")
    return redirect("my_products")


@login_required
def my_self(request):
    return render(request, "my_self.html", {"myself": request.user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("my_self")
    else:
        form = UserForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": form})
