from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from clients import models
from django.urls import reverse_lazy

class Read(ListView):
    model = models.UserAccount
    context_object_name = 'clients'
    template_name = 'clients/ListView.html'

class Create(CreateView):
    model = models.UserAccount
    template_name = 'clients/CreateView.html'
    fields = ['user','password','name','surname']
    success_url = reverse_lazy('listview')

class Update(UpdateView):
    model = models.UserAccount
    template_name = 'clients/UpdateView.html'
    fields = ['user','password','name','surname']
    success_url = reverse_lazy('listview')

class Delete(DeleteView):
	model = models.UserAccount
	template_name = 'clients/DeleteView.html'
	success_url = reverse_lazy('listview')

class Details(DetailView):
    model = models.UserAccount
    template_name = 'clients/DetailsView.html'