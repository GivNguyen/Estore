from django.urls import path
from .views import *

app_name = 'customers'
urlpatterns = [
    path('signup/', dang_ky, name='dang_ky'),
    path('login/', dang_nhap, name='dang_nhap'),
    path('myaccount/', my_account, name='my_account'),
    path('signout/', dang_xuat, name='dang_xuat'),
]