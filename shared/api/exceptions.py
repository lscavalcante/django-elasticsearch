from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

'''
400 will be used for validation errors.
401 for auth errors.
403 for permission errors.
404 for not found errors.
429 for throttling errors.
500 for server errors (we need to be careful not to silence an exception causing 500 and always report that in services like Sentry)
'''


class ValidationErrors(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('ValidationErrors')
    default_code = 'validation_errror'


class RuleException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('RuleException')
    default_code = 'rule_exception'


class ServerFailure(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('ServerFailure')
    default_code = 'server_failure'


class ObjectNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('ObjectNotFound')
    default_code = 'object_notfound'


class AuthErrors(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('AuthErrors')
    default_code = 'auth_errors'


class PermissionErrors(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('PermissionErrors')
    default_code = 'permission_errors'


class NotFoundErrors(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('NotFoundErrors')
    default_code = 'not_found_errors'


class ThrottlingErrors(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = _('ThrottlingErrors')
    default_code = 'throttling_errors'


class ServerErrors(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('ServerErrors')
    default_code = 'server_errors'
