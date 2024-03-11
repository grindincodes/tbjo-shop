from django.shortcuts import *
from .forms import *
from .models import *
from django.core.exceptions import ValidationError

# Create your views here.
def order(request, product_pk):
    if not request.user.is_authenticated:
        return redirect('email_login')
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            order.save()
            return redirect('complete', order_pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form':form, 'product':product})

def complete(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    product = get_object_or_404(Product, pk=order.product.pk)
    if not request.user.is_authenticated:
        return redirect('email_login')
    if order.user != request.user:
        raise ValidationError("잘못된 접근입니다.")   
    return render(request, 'complete.html', {'order':order,'product':product})

def all(request):
    if not request.user.is_authenticated:
        return redirect('email_login')
    orders = Order.objects.filter(user=request.user)
    # products = Product.objects.
    # for order in orders:
    #     product = Product.objects.get(pk=order.product.pk)

    # orders = get_list_or_404(Order, user=request.user)
    return render(request, 'all.html', {'orders':orders})