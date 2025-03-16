import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Customer, Category, Product, Cart, CartItem, Order, OrderItem, Vendor
from .forms import VendorRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

@login_required
def user_home(request):
    orders = Order.objects.filter(customer__user=request.user).order_by('-created_at')
    return render(request, 'shop/user_home.html', {'orders': orders})

def vendor_details(request):
    if not request.user.is_authenticated:
        return redirect('login')
    vendors = Vendor.objects.all()
    return render(request, 'shop/vendor_details.html', {'vendors': vendors})

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = VendorRegistrationForm()
    return render(request, 'shop/vendor_register.html', {'form': form})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/product_list.html', {
        'categories': Category.objects.all(),
        'selected_category': category,
        'products': products,
    })

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'categories': categories, 'products': products})

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect("login")
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    user = request.user
    customer, created = Customer.objects.get_or_create(user=user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

def place_order(request):
    customer = request.user.customer
    cart = Cart.objects.get(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(customer=customer, total_price=total_price)
    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
    cart_items.delete()
    return redirect('order_detail', order_id=order.id)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'shop/order_detail.html', {'order': order, 'order_items': order_items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not Customer.objects.filter(user=user).exists():
                customer = Customer.objects.create(user=user)
                Cart.objects.create(customer=customer)
                login(request, user)
                return redirect('home')
            else:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def payment_success(request):
    print(request.method)
    return render(request, 'shop/payment_success.html')

@csrf_exempt
def payment_verification(request, order_id):
    if request.method == "POST":
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        order = get_object_or_404(Order, id=order_id)

        params_dict = {
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_order_id": razorpay_order_id,
            "razorpay_signature": razorpay_signature,
        }

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))  # Initialize client here

        try:
            client.utility.verify_payment_signature(params_dict)
            print("payment_verification : redirecting with GET")
            return redirect("payment_success")
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Payment verification failed")
    else:
        return HttpResponseBadRequest("Invalid request method")