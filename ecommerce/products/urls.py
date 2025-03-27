from django.urls import path
from .import views 

urlpatterns = [
    path('',views.product, name='product'),
    path('/productdetail', views.productDetail, name='productDetail'),
    
]
