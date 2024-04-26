from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Product, Wishlist
from django.http import JsonResponse

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': wishlist}
    return render(request, 'store/wishlist.html', context)


def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.filter(id=prod_id).first()
            if product_check:
                if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return JsonResponse({'status': "Invalid request method"})


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                wishlist_item = Wishlist.objects.get(user=request.user, product_id=prod_id)
                wishlist_item.delete()
                return JsonResponse({'status': "Product removed from wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')