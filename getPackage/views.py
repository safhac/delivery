from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.db.models import Sum
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from app.models import *
from app.forms import *



class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'getPackage/home.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if Sender.objects.filter(user=self.request.user).count() > 0:
                context['user_type'] = 'sender'
                context['deliveries'] = Delivery.objects.all()
                context['couriers'] = Courier.objects.all()
            else:
                context['user_type'] = 'courier'
                as_courier = Courier.objects.get(user=self.request.user)
                context['deliveries'] = Delivery.objects.filter(courier=as_courier)
                context['total'] = context['deliveries'].aggregate(Sum('cost'))
                
        return context    

class AddDelivery(CreateView):
    template_name = 'getPackage/new_delivery.html'
    form_class = DeliveryForm
    def form_valid(self, form):
        delivery = form.save(commit=True)
        delivery.save()
        return redirect('home')


def SetCourierDelivery(request, pk, id):
    delivery = get_object_or_404(Delivery, pk=pk)
    courier = get_object_or_404(Courier, pk=id)
    # print("{} {}".format(courier, type(courier)))
    delivery.courier = courier
    delivery.save()
    return redirect('home')