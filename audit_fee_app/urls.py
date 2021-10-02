from django.urls import path
from audit_fee_app import views

urlpatterns = [
    path("<int:audit_fee_id>/", views.audit_fee_detail, name="audit_fee_detail"),
]
