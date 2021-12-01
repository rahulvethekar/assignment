from django.urls import path
from .views import create_product,update_product,all_product

urlpatterns = [
    path('create_prod/',create_product,name = 'create_prods'),
    path('all_prods/',all_product,name = 'all_product'),
    path('update_prods/<int:uid>',update_product,name = 'update_product'),

]
