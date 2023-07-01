from django.db import models
from django.urls import reverse

class cdetails (models.Model):
    CustId = models.CharField(max_length=255, null=False)
    CName = models.CharField(max_length=255, null=False)
    PhoneNum = models.CharField(max_length=255, null=False)
    Email = models.EmailField(max_length=255, null=False)
    Adrs = models.CharField(max_length=255,null=False)

    # str
    def __str__(self):
        return self.PhoneNum
    def get_absolute_url(self):
        return reverse("cust-list")
