from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from store.models import Product, Cart
from django.contrib.auth.decorators import login_required

def addtocart(request):
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                prod_id = int(request.POST.get('product_id'))
                product_check = Product.objects.filter(id=prod_id).first()
                if product_check:
                    if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                        return JsonResponse({'status': "Product Already in Cart"})
                    else:
                        prod_qty = int(request.POST.get('product_qty'))
                        if product_check.quantity >= prod_qty:
                            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                            return JsonResponse({'status': "Product added successfully"})
                        else:
                            return JsonResponse({'status': "Only " + str(product_check.quantity) + " quantity available"})
                else:
                    return JsonResponse({'status': "No such product found"})
            else:
                return JsonResponse({'status': "Login to Continue"})
    except Exception as e:
        return JsonResponse({'status': "Error occurred: " + str(e)})  # Handle exceptions and return an error response

@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render (request, "store/cart.html", context)


from django.http import JsonResponse
from django.shortcuts import redirect
from store.models import Cart

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated Successfully"})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status': "Deleted Successfully"})
    return redirect('/')
