from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Page

class HomeView(ListView):
    model = Page
    template_name = 'index.html'
    success_url = 'homepage'

class PageView(DetailView):
    model = Page
    template_name = 'page-detail.html'

# Create your views here.
