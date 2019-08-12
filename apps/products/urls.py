from django.urls import path
from .views import ProductListView, ProductDetailView, CaseListView,CaseDetailView

app_name = 'products'

urlpatterns =[
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('cases/', CaseListView.as_view(), name='case_list'),
    path('cases/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
]