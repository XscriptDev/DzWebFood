from attr import s
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from numpy import product

import codebarapp
import openfoodfacts as client
import pandas as pd

from codebarapp.models import Product
from django.contrib import messages
from .models import Product
from .forms import ProductForm
# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def ajax(request):
    if request.method == "POST":
        codebar = request.POST.get('Codebar')
        print(codebar)
        product_dict = client.get_product(str(codebar), locale='dz')['product']
        return JsonResponse({'ProductName': product_dict['product_name_fr'] if product_dict.get('product_name_fr')!=None else product_dict['product_name'], 'BarCode':product_dict['_id'], 'Brand': product_dict['brands'], 'Image': product_dict['image_url'], 'ref': product_dict['quantity']})
    
@csrf_exempt
def retrieve(request):
    if request.method == "POST":
        """ Pname = request.POST.get('productname')
        Pbrand = request.POST.get('brand')
        Pref = request.POST.get('ref')
        codebar = request.POST.get('codebar')
        product = Product.objects.update_or_create(codebar = codebar, defaults = dict(codebar = codebar, productName = Pname, brand = Pbrand, ref = Pref),) """
        
        messages.success(request, "Created successfully")
        messages.warning(request, 'error happened')
        print(Product.objects.all())
        return render(request,'index.html')


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return HttpResponseRedirect(request, '/product/edit')
        else:
            for error in form.errors:
                messages.warning(error)
    else:
        form = ProductForm()
    return render(request,'index.html',locals())


