"""
WSGI config for audit_fee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# herokuでGunicornなどのWSGIサーバーを使用して本番環境から静的ファイルを適用するのに必要。
from dj_static import Cling

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'audit_fee.settings')

application = Cling(get_wsgi_application())
