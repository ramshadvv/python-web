from django.db import models
from datetime import datetime

# Create your models here.

class SkuTable(models.Model):
    docstatus                 = models.BooleanField(default=False, null=True, blank=True)
    doctype                   = models.CharField(max_length=255, null=True, blank=True)
    idx                       = models.IntegerField(null=True, blank=True)
    modified_by               = models.EmailField(null=True, blank=True)
    owner                     = models.EmailField(unique=True, null=True, blank=True,max_length=255)
    name                      = models.CharField(max_length=255, null=True, blank=True)
    parent                    = models.CharField(max_length=100, null=True, blank=True)
    parentfield               = models.CharField(max_length=100, null=True, blank=True)
    parenttype                = models.CharField(max_length=100, null=True, blank=True)
    quantity                  = models.BigIntegerField(null=True, blank=True)
    sku                       = models.CharField(max_length=255,primary_key=True)
    sku_description           = models.CharField(max_length=255, null=True, blank=True)
    standard_crate_quantity   = models.CharField(max_length=255, null=True, blank=True)

    creation        =   models.DateTimeField(default=datetime.now())
    modified        =   models.DateTimeField(auto_now_add=True)

class  CrateTable(models.Model):
    crate            = models.CharField(max_length=255, null=True, blank=True)
    crate_weight     = models.BigIntegerField(null=True, blank=True)
    docstatus        = models.BooleanField(default=True, null=True, blank=True)
    doctype          = models.CharField(max_length=255, null=True, blank=True)
    idx              = models.IntegerField(null=True, blank=True)
    is_final_crate   = models.BooleanField(default=False, null=True, blank=True)
    modified_by      = models.EmailField(null=True, blank=True)
    name             = models.CharField(max_length=255, null=True, blank=True)
    owner            = models.EmailField(null=True, blank=True)
    packed_quantity  = models.IntegerField(null=True, blank=True)
    parent           = models.CharField(max_length=100, null=True, blank=True)
    parentfield      = models.CharField(max_length=100, null=True, blank=True)
    parenttype       = models.CharField(max_length=100, null=True, blank=True)
    sku              = models.ForeignKey(SkuTable, on_delete=models.CASCADE, null=True, blank=True)

    creation         =   models.DateTimeField(default=datetime.now())
    modified         =   models.DateTimeField(auto_now_add=True)

