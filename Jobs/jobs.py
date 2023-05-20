from django.conf import settings
import requests
import json
import random

from Deals.views import *
from django.utils import timezone

def ExpireDeals():
    current_time = timezone.now()
    data=deal.objects.filter(expired=False)
    for m in range(0,len(data)):
        if data[m].expired_at<=timezone.now():
            deal.objects.filter(Product_name=data[m].Product_name).update(expired=True)
            print(data[m].Product_name)

        
            

            

