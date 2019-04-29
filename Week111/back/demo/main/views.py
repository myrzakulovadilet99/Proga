from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from shop.views import Category
# Create your views here.


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_list.html', context)


def index(request):
    context = {
        'name': 'Student 1',
        'nums': [i for i in range(5)],
        'is_logged_in': False,
        'product': {
            'id': 1,
            'name': 'Product 1'
        },
        'products': [{
            'id': i,
            'name': 'Product {}'.format(i)
        } for i in range(5)]
    }
    return render(request, 'index.html', context)

# def about(request):
#     return HttpResponse('<h1>Isddsfg </h1>')

def about(request):
    return render(request, 'about.html')

def current_time(request):
    return HttpResponse('<h1>{}</h1>.'.format(datetime.now()))


def current_time_plus(request, num):
    return HttpResponse('arg number: {}'.format(num))

def show_product(request, pk):
    return HttpResponse('<h1>{}</h1>'.format(pk))