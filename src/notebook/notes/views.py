from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .utils import Mymixin
from .models import Note


class HomeView(Mymixin, ListView):
    model = Note
    template_name = 'notes/index.html'
    context_object_name = 'notes'
    mixin_prop = ''
    #paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_prop'] = self.mixin_func()
        return context

    def get_queryset(self):
        return Note.objects.order_by('-updated').select_related('category')
