from attr import s
from django.shortcuts import get_object_or_404, render, HttpResponse
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
        return JsonResponse({'ProductName': product_dict.get('product_name_fr') if product_dict.get('product_name_fr')!=None else product_dict.get('product_name'), 'BarCode':product_dict.get('_id'), 'Brand': product_dict.get('brands'), 'Image': product_dict.get('image_url'), 'ref': product_dict.get('quantity')})
    
@csrf_exempt
def retrieve(request):
    if request.method == "POST":
        Pname = request.POST.get('productName')
        Pbrand = request.POST.get('brand')
        Pref = request.POST.get('ref')
        codebar = request.POST.get('codebar')
        product = Product.objects.update_or_create(codebar = codebar, defaults = dict(codebar = codebar, productName = Pname, brand = Pbrand, ref = Pref),)
        
        messages.success(request, "Created successfully")
        messages.warning(request, 'error happened')
        print(Product.objects.all())
        return HttpResponseRedirect('/product/list')


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        print('yes')
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
        
            return HttpResponseRedirect('/product/list')
        else:
            for error in form.errors:
                messages.warning(request,error)
                #need to implement this in the HTML template
            context={}
            context['form'] = form       
            return render(request,'addProduct.html',context)
    else:
        form = ProductForm()
        context={}
        context['form'] = form       
        return render(request,'addProduct.html',context)
    


@csrf_exempt
def modify_product(request, id):
        if request.method == "POST":
        # Update View for Details
        #fetch the object related to passed id
            obj = get_object_or_404(Product, id = id)

            #pass the object as instance in form
            form = ProductForm(request.POST or None, instance = obj)
            if form.is_valid():
                form.save()

            return render(request, "")
@csrf_exempt        
def list_product(request):
    context = {}
    
    context['dataset'] = Product.objects.all()
    
    return render(request, "list.html", context)


@csrf_exempt
def view_product(request,id):
    context = {}
    
    context["data"] = Product.objects.get(codebar = id)
    return render(request,"view.html",context)

@csrf_exempt
def update_product(request,id):
    if request.method == "POST":
        context = {}
        obj = get_object_or_404(Product,codebar=id)
        form = ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product/'+id)
        else:
            return HttpResponseRedirect('/product/'+id+'/edit')
    else:
        context = {}
        context["data"] = Product.objects.get(codebar = id)
        return render(request,"edit.html",context)
    
    
