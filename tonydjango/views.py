from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def blogpage(request):
    return render(request, 'blog.html')

def contactpage(request):
    return render(request, 'contact.html')

def productspage(request):
    return render(request, 'products.html')

