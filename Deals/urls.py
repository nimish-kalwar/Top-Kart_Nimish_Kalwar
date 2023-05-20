from django.urls import path,include
from . import views

urlpatterns = [
    path('create-deal/', views.CreateDeal.as_view(), name='create-deal'),
     path('create-order/', views.CreateOrder.as_view(), name='create-order'),
      path('update-order/', views.UpdateOrder.as_view(), name='update-order'),
      path('fetch-deals/', views.FetchDeals.as_view(), name='fetch-deals'),
      path('track-status/', views.TrackStatus.as_view(), name='track-status'),
      
]