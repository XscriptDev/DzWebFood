from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from numpy import product

import codebarapp
import openfoodfacts as client
import pandas as pd
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
        return JsonResponse({'ProductName':product_dict['product_name'], 'BarCode':product_dict['_id'], 'Brand': product_dict['brands']})