from audit_fee_app.models import Audit_fee
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

import pandas as pd

from django.db.models import Q
from django.db.models import Count
from django.db.models import Max

def top(request):
    audit_fee = Audit_fee.objects.all()
    audit_firm = Audit_fee.objects.values('auditor').annotate(dcount=Count('auditor'))

    keyword = request.GET.getlist("office")
    keyword2 = request.GET.get("query")
    print(keyword,keyword2)

    if keyword or keyword2:
        audit_fee = audit_fee.filter(
            Q(auditor__in=keyword) & Q(kam_title_1__icontains=keyword2) 
        )
    
    df = pd.DataFrame(list(audit_fee.values()))
    print(df)

    context = {
        'audit_fee':audit_fee,
        'audit_firm':audit_firm,
        }
    return render(request,'audit_fee_app/top.html',context)

def audit_fee_detail(request,audit_fee_id):
    audit_fee = get_object_or_404(Audit_fee, pk=audit_fee_id)
    return render(request,'audit_fee_app/audit_fee_detail.html',{'audit_fee':audit_fee})

