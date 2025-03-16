import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

# Initialize Razorpay Client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create({
        "amount": int(order.total_price * 100),  # Convert to paisa
        "currency": "INR",
        "payment_capture": "1"  # Auto-capture payment
    })

    # Pass order details to template
    return render(request, "shop/payment.html", {
        "order": order,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
    })