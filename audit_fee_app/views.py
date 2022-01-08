from audit_fee_app.models import Audit_fee
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

import pandas as pd

from django.db.models import Q
from django.db.models import Count
from django.db.models import Max


# Googleスプレッドシートとの連携に必要なライブラリ
import gspread
from dotenv import find_dotenv, load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import os

# 設定
file_name = 'audit-fee-bot'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# .envファイルを探して読み込む
load_dotenv(find_dotenv())

# 辞書オブジェクト。認証に必要な情報をHerokuの環境変数から呼び出している
credential = {
"type": "service_account",
"project_id": os.environ['SHEET_PROJECT_ID'],
"private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
"private_key": os.environ['SHEET_PRIVATE_KEY'],
"client_email": os.environ['SHEET_CLIENT_EMAIL'],
"client_id": os.environ['SHEET_CLIENT_ID'],
"auth_uri": "https://accounts.google.com/o/oauth2/auth",
"token_uri": "https://oauth2.googleapis.com/token",
"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
"client_x509_cert_url":  os.environ['SHEET_CLIENT_X509_CERT_URL']
}
# スプレッドシートにアクセス
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
gc = gspread.authorize(credentials)
sh = gc.open(file_name)

# シートから全部から読み込み
def get_records(wks):
    record = pd.DataFrame(wks.get_all_records())
    return record

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
    print(type(df))

    wks5 = sh.worksheet('save_data')
    df5 = get_records(wks5).head(10)
    print(df5)

    context = {
        'audit_fee':audit_fee,
        'audit_firm':audit_firm,
        }
    return render(request,'audit_fee_app/top.html',context)

def audit_fee_detail(request,audit_fee_id):
    audit_fee = get_object_or_404(Audit_fee, pk=audit_fee_id)
    return render(request,'audit_fee_app/audit_fee_detail.html',{'audit_fee':audit_fee})

