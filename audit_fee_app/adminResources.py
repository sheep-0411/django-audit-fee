from import_export import resources

from .models import Audit_fee


class Audit_feeResource(resources.ModelResource):

    class Meta:
        model = Audit_fee
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('edinet_code','end_date' )