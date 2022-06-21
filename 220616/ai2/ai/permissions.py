from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from datetime import timedelta, datetime
from django.utils import timezone


class RegisterdMoreThanThreeDaysUser(BasePermission):
    ''' 
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    '''

    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        user = request.user
        # 함축식 조건 1) 로그인 사용자인가 조건 2) 가입일 기준 3일이 지났는가
        return bool(user.is_authenticated and request.user.join_date < (timezone.now() - timedelta(seconds=3)))

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    '''
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    '''
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 아닙니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                "detail" : "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        if user.is_authenticated and user.is_admin or \
            user.join_date < (datetime.now().date() - timedelta(days=7)):
            return True

        return False