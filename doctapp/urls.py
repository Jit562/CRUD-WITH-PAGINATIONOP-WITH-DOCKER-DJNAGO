from django.urls import path
from .views import ProductView, ProductAdd, delete_data, update_data

urlpatterns = [
    path('', ProductView, name='product'),
    path('productadd/', ProductAdd, name='productadd'),
    path('delete_data/<int:id>/', delete_data, name='delete_data'),
    path('update_data/<int:id>/', update_data, name='update_data'),
]
