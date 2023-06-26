from django.urls import path
from  .views import *

urlpatterns = [
    path('itams/', ItemsView, name='itams'),
]