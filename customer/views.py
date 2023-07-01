from customer.models import cdetails
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class CustCreateView (CreateView):
    template_name = 'customer/create_cust.html'
    model = cdetails
    fields = ('CustId','CName','PhoneNum','Email','Adrs')

class CustDetailView (DetailView):
    template_name = 'customer/custdetail.html'
    model = cdetails
    context_object_name = 'Cust_detail'

class CustListView (ListView):
    template_name = 'customer/custlist.html'
    model = cdetails
    context_object_name = 'CustList'
    
class CustDeleteView (DeleteView):
    model = cdetails
    success_url = reverse_lazy('cust-list')

class CustUpdateView(UpdateView):
    model = cdetails 
    fields = ('CustId','CName','PhoneNum','Email','Adrs')
    success_url = reverse_lazy('profileupdate')  
      
def customer_updation_success(request):
    return render(request,"customer/cdetails_updation_success.html")
