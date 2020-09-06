from django.urls import path, include
from .views import (
    Home,
    Reg
)

app_name= 'customer'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('reg/', Reg.as_view(), name='reg'),
]