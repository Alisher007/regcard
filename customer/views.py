from django.shortcuts import render
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = 'customer/home.html'
    
class Reg(TemplateView):
    template_name = 'customer/reg.html'