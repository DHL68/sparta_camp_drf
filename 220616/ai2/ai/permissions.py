from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class RegisterdMoreThanThreeDaysUser(BasePermission):
    ''' 
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    '''

    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        user = request.user
        # 함축식 조건 1) 로그인 사용자인가 조건 2) 가입일 기준 3일이 지났는가
        return bool(user.is_authenticated and request.user.join_date < (timezone.now() - timedelta(days=3)))
