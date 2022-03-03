from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Orders, Products
import json 

# Create your views here.
class Create_Order(APIView):
    """
        API to create orders and store them in DB
    """

    def post(self, request):
        


        return Response("Successfully created an order!")


class Upload_Products(APIView):
    """
        API to upload products. 
        Should be accessible only by admin. 
        Should overwrite the price of a product if it already exists in the DB. 
    """    

    def post(self, request):
        # import pdb; 
        # pdb.set_trace()
        response = "Failure! Please check request"
        product_name = request.data['name']
        prod_obj = Products.objects.filter(product_name=product_name)
        if prod_obj:
            prod_obj.price = request.data['price']
            prod_obj.quantity = request.data['quantity']
            response = "Successfully updated products to catalog"
        else: 
            product_name = product_name
            price = request.data['price']
            quantity = request.data['quantity']
            new_prod = Products.objects.create(
                product_name=product_name,
                price=price,
                quantity=quantity
            )
            response = "Successfully added products to catalog"

        return Response(response)


class View_Products(APIView):
    """
        API to view all products stored in DB
    """
    def get(self, request):
        res = []
        for prod in Products.objects.all():
            # res.append( [ 'name':prod.name, 'price': prod.price'': 'quantity': prod.quantity])
            item = {'name':prod.product_name, 'price': prod.price, 'quantity': prod.quantity}
            res.append(item)
        return Response(res)
