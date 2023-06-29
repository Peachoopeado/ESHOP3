from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created, order_notification
from django.contrib.auth.decorators import login_required




# Create your views here.
def order_create(request):
    cart = Cart(request)
    error = ''
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            else: 
                order.user = None
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            data = {
                'order': order,
            }
            order_created(order.id)
            order_notification(order.id)

            return render(request, 'orders/order/created.html', data)
        else:
            error = 'ОШИБКА'
    else:
        form = OrderCreateForm()

    data = {
        'cart': cart,
        'form': form,
        'error': error
    }
    return render(request, 'orders/order/create.html', data)
