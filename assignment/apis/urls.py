from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.Create_Order.as_view(), name='create_order'),
    path('upload_products/', views.Upload_Products.as_view(), name='upload_products' ),
    path('view_products/', views.View_Products.as_view(), name='view_products')
]

app_name = 'apis'