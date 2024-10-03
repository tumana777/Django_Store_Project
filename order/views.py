from django.shortcuts import HttpResponse

def order_list(request):
    return HttpResponse("<h3>Here are all orders:</h3>")

def order_detail(request, order_id):
    return HttpResponse("<h3>Here must be order details :)</h3>")
