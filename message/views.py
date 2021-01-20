from django.shortcuts import render

# Create your views here.
from .models import Dialer
from django.views.generic import ListView,DetailView,FormView

from .forms import Contact,Message 
from django.urls import reverse_lazy
from .utils import send
from django.http import HttpResponse


class ContactList(ListView):
   model=Dialer
   template_name='message/home.html'


class MessageContactList(DetailView):
    model=Dialer
    template_name='message/detail.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=Message
        return context

    def post(self,request,*args,**kwargs):
        form=Message(request.POST)
        if form.is_valid():
            message_to=self.get_object()
            body=form.cleaned_data.get('body')
            send(body,message_to)
            return HttpResponse(f"we have send message {body} to {message_to}")

class AddContact(FormView):
    form_class=Contact
    template_name='message/add.html'
    success_url=reverse_lazy('message:contact-list')