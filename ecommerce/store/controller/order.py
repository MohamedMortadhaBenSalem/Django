from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Order, OrderItem

@login_required
def index(request):
    orders = Order.objects.filter(user=request.user)  # Corrected the dash to a dot
    context = {'orders': orders}
    return render(request, "store/orders/index.html", context)

@login_required
def view_order(request, t_no):  # Corrected the function name to follow snake_case convention
    order = Order.objects.filter(tracking_no=t_no, user=request.user).first()  # Corrected the dash to a dot
    order_items = OrderItem.objects.filter(order=order)  # Corrected the variable name to follow snake_case convention
    context = {'order': order, 'order_items': order_items}  # Corrected the variable name to follow snake_case convention
    return render(request, "store/orders/view.html", context)  # Corrected the quotation mark and variable name
