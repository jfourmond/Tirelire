from rest_framework.exceptions import APIException


class BrokenBankException(APIException):
    status_code = 406
    default_detail = 'Your piggy bank is broken. Please create another.'
    default_code = 'broken_piggy_bank'


class IntactBankException(APIException):
    status_code = 406
    default_detail = 'Your piggy bank is intact.'
    default_code = 'intact_piggy_bank'
