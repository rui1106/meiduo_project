from django.urls import path, re_path

from . import views
# from meiduo_mall.meiduo_mall.apps.verifications.views import SMSCodeView

urlpatterns = [
    re_path(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
]
