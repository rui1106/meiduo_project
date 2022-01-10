import random

from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.response import Response

from rest_framework.views import APIView

import logging

logger = logging.getLogger('django')


class SMSCodeView(APIView):
    def get(self, request, mobile):
        # 创建连接到redis的对象
        redis_conn = get_redis_connection('verifications')

        sms_code = '%06d' % random.randint(0, 999999)

        redis_conn.setex('sms_%s' % mobile, 300, sms_code)

        logger.info(sms_code)

        return Response({'message': 'ok'})
