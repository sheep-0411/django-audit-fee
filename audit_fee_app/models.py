from django.conf import settings
from django.db import models
from django.utils import timezone

class Audit_fee(models.Model):
    edinet_code = models.CharField('EDINETコード', max_length=128)
    name = models.CharField('会社名', max_length=128)
    end_date = models.DateField('期末日',blank=True)
    filling_date = models.DateField('提出日',blank=True)
    fiscal_year = models.CharField('事業年度', max_length=128)
    audit_fee = models.IntegerField('監査報酬', blank=True)
    audit_fee_networkfirm = models.IntegerField('監査報酬(ネットワークファーム)', blank=True,null=True)
    auditor = models.CharField('監査法人',max_length=128)
    kam_title_1 = models.CharField('KAM1', max_length=128, blank=True,null=True)
    kam_title_2 = models.CharField('KAM2', max_length=128, blank=True,null=True)
    kam_title_3 = models.CharField('KAM3', max_length=128, blank=True,null=True)
    kam_title_4 = models.CharField('KAM4', max_length=128, blank=True,null=True)
    kam_title_5 = models.CharField('KAM5', max_length=128, blank=True,null=True)
    kam_description_1 = models.TextField('KAM1の内容及び決定理由', blank=True,null=True)
    kam_description_2 = models.TextField('KAM2の内容及び決定理由', blank=True,null=True)
    kam_description_3 = models.TextField('KAM3の内容及び決定理由', blank=True,null=True)
    kam_description_4 = models.TextField('KAM4の内容及び決定理由', blank=True,null=True)
    kam_description_5 = models.TextField('KAM5の内容及び決定理由', blank=True,null=True)
    kam_audit_description_1 = models.TextField('KAM1の監査上の対応', blank=True,null=True)
    kam_audit_description_2 = models.TextField('KAM2の監査上の対応', blank=True,null=True)
    kam_audit_description_3 = models.TextField('KAM3の監査上の対応', blank=True,null=True)
    kam_audit_description_4 = models.TextField('KAM4の監査上の対応', blank=True,null=True)
    kam_audit_description_5 = models.TextField('KAM5の監査上の対応', blank=True,null=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.name