from django.shortcuts import render
from accounts.models import Accounts
from .models import *

# Create your views here..

def homepage(request):
    user = Accounts.objects.get(owner='grn@iotready.co')
    procured_quantity = 0
    for i in user.crate_table.all():
        procured_quantity += i.packed_quantity
    context = {
        'item':user,
        'procured_quantity':procured_quantity
    }
    return render(request, 'index.html', context)
