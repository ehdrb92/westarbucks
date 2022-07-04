from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from products.models import Menu, Category, Drink

class ProductsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        menu1     = Menu.objects.create(name=data['menu'])
        category1 = Category.objects.create(
            name = data['categories'],
            menu = menu1
        )
        Drink.objects.create(
            korean_name = data['drinks'], 
            category = category1
        )

        return JsonResponse({'messasge':'created'}, status=201)

class ProductsView(View):
    def get(self, request):
        products = Drink.objects.all()
        results  = []

        for drink in products:
           results.append(
               {
                   "menu" : drink.category.menu.name,
                   "category" : drink.category.name,
                   "product_name" : drink.korean_name
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)