from django.contrib import admin
from audit_fee_app.models import Audit_fee

from import_export.admin import ImportExportModelAdmin
from .adminResources import Audit_feeResource

# Register your models here.

#admin.site.register(Audit_fee)
@admin.register(Audit_fee)
class Audit_feeAdmin(ImportExportModelAdmin):
    resource_class = Audit_feeResource