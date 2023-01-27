from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from userapp.models import *

# Create your CustomManager here.

class AccountManager(BaseUserManager):
    def _create_user(self, owner, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not owner:
            raise ValueError('The given email must be set')
        user = self.model(
            owner=owner,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, owner, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(owner, password, **extra_fields)


    def create_superuser(self, owner, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(owner, password, **extra_fields)


# Create your models here.


class Accounts(AbstractUser,PermissionsMixin):
    owner           = models.EmailField(primary_key=True, unique=True,max_length=255)
    username        = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name            = models.CharField(max_length=255, null=True, blank=True)
    docstatus       = models.BooleanField(default=True)
    doctype         = models.CharField(max_length=100, null=True, blank=True)
    grn             = models.CharField(max_length=100, null=True, blank=True)
    hub             = models.CharField(max_length=100, null=True, blank=True)
    idx             = models.IntegerField(default=0)
    modified_by     = models.EmailField(null=True, blank=True)
    parent          = models.CharField(max_length=100, null=True, blank=True)
    parentfield     = models.CharField(max_length=100, null=True, blank=True)
    parenttype      = models.CharField(max_length=100, null=True, blank=True)
    supplier        = models.CharField(max_length=100, null=True, blank=True)
    supplier_name   = models.CharField(max_length=100, null=True, blank=True)
    crate_table     = models.ManyToManyField(CrateTable, blank=True)
    sku_table       = models.ManyToManyField(SkuTable, blank=True)

    #required

    creation        =   models.DateTimeField(default=datetime.now())
    modified        =   models.DateTimeField(auto_now_add=True)
    is_staff        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=True)
    is_superuser    =   models.BooleanField(default=False)
    

    object = AccountManager()
    USERNAME_FIELD = 'owner'
    

    class meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
