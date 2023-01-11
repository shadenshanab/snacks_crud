from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy


class HomePage(TemplateView):
    template_name='home.html'

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetail(DetailView):
    template_name='snack_detail.html'
    model=Snack

class SnackCreate(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "description", "purchaser"]


class SnackUpdate(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "description", "purchaser"]



class SnackDelete(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snacks")