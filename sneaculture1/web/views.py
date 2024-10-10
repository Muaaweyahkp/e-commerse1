from django.shortcuts import render

def index(request):
    return render (request, 'web/index.html')
def blog(request):
    return render (request, 'web/blog.html')
def contact(request):
    return render (request, 'web/contact.html')
def category(request):
    return render (request, 'web/category.html')
def cart(request):
    return render (request, 'web/cart.html')
def checkout (request):
    return render (request, 'web/checkout.html')
def confirmation(request):
    return render (request, 'web/confirmation.html')
def singleProduct(request):
    return render (request, 'web/single-product.html')
def tracking(request):
    return render(request,'web/tracking.html')
def login(request):
    return render(request, 'web/login.html')
def elements(request):
    return render(request, 'web/elements.html')
def singleBlog(request):
    return render(request, 'web/single-blog.html')
