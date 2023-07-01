from django.urls import path
from customer import views

urlpatterns = [
    path('create-customer' , views.CustCreateView.as_view(), name='create-customer'),
    path('cust-list' , views.CustListView.as_view(), name='cust-list'),
    path('<int:pk>' , views.CustDetailView.as_view(), name='cust-detail'),
    path('delete=<int:pk>' , views.CustDeleteView.as_view(), name='delete'),
    path('customer_updation_success',views.customer_updation_success,name='profileupdate'),
    path('update=<int:pk>',views.CustUpdateView.as_view(),name='update'),
]   