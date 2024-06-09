from django.urls import path
# Импортируем созданное нами представление
from .views import (ProductsList, ProductDetail,CategoryDetail, ProductCreate, ProductUpdate, ProductDelete) #create_product


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('products/', ProductsList.as_view(), name='product_list'),
   path('products/<int:pk>', ProductDetail.as_view(), name ='product_detail'),
   path('category/<int:pk>', CategoryDetail.as_view(), name = 'category_detail'),
   # path('products/create/', create_product, name = 'product_create'),
   path('products/create/', ProductCreate.as_view(), name='product_create'),
   path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]
