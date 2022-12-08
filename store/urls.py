from django.urls import path
from .views import *


app_name = 'store'
urlpatterns = [
    path('', trang_chu, name='trang_chu'),
    path('trang-chu-2/', trang_chu_2, name='trang_chu_2'),
    path('san-pham', san_pham, name='san_pham'),
]
