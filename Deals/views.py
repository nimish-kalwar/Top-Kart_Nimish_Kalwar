from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
import os
import json
import datetime
from rest_framework.views import APIView
import random
import string
from Deals.models import *
from rest_framework.response import Response

# API's for seller
class CreateDeal(APIView):
    permission_classes = []
    def post(self, request):
        d={"Status":"Deal Created"}
        exp_at =  timezone.now() + datetime.timedelta(days=1/2)
        pid='1' + ''.join(random.choice(string.digits) for i in range(5))
        deal.objects.create(
            Product_id=pid,
            Product_name=request.data["product_name"],
            Actual_price=request.data["actual_price"],
            Final_price=request.data["discounted_price"],
            Total_units = request.data["units"],
            Available_units = request.data["units"],
            expired_at=exp_at
        )

        return Response(d)

class UpdateOrder(APIView):
    permission_classes = []
    def post(self, request):
        d={"Status":"Failed to update"}
       
        if Orders.objects.filter(Product_name=request.data["product_name"]).exists()==True:
            Orders.objects.filter(Product_name=request.data["product_name"]).update(status='Approved')
            d={"Status":"updated"}
        else:
            d={"Status":"Order doesn't exist"}

        return Response(d)

# API's for customer
class CreateOrder(APIView):
    permission_classes = []
    def post(self, request):
        d={"Status":"Deal don't exist/Expired"}
       
        oid='5' + ''.join(random.choice(string.digits) for i in range(9))
        if deal.objects.filter(Q(Product_name=request.data["product_name"]) & Q(expired=False)).exists()==True:
            if int(deal.objects.get(Product_name=request.data["product_name"]).Available_units)>=int(request.data["quantity"]):
                Orders.objects.create(
                    order_id=oid,
                    Product_name=request.data["product_name"],
                    Product_id=deal.objects.get(Product_name=request.data["product_name"]).Product_id,
                    Ordered_price=request.data["price"],
                    buyer_name=request.data["buyer_name"],
                    quantity=request.data["quantity"]
                )
                q=int(deal.objects.get(Product_name=request.data["product_name"]).Total_units)-int(request.data["quantity"])
                deal.objects.filter(Product_name=request.data["product_name"]).update(Available_units=q)
                d={"Status":"Product Ordered"}
            else:
                d={"Status":"Out of stock"}

        return Response(d)

class FetchDeals(APIView):
    permission_classes = []
    def get(self, request):
        
        m=deal.objects.filter(expired=False).values('Product_name','expired_at','Actual_price','Final_price','Available_units')

        return Response(m)

class TrackStatus(APIView):
    permission_classes = []
    def post(self, request):
        m=[]
        if Orders.objects.filter(Product_name=request.data["product_name"]).exists()==True:
            m=Orders.objects.filter(Product_name=request.data["product_name"]).values('status')

        return Response(m)