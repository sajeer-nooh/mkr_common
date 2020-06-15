from mkr_common.constants.message import NOT_FOUND_404


class LogException:
    def __init__(self, error_message):
        self.error_message = error_message

    def log_warning(self):
        print("Warning: %s" % self.error_message)

    def log_error(self):
        print("Error: %s" % self.error_message)

    def log_info(self):
        print("Info: %s" % self.error_message)


class BaseCustomException(Exception):
    status_code = None
    error_message = None
    error_code = None

    def __init__(self, error_message):
        Exception.__init__(self)
        self.error_message = error_message
        self.error_code = error_code

    def to_dict(self):
        LogException("Code: %s, Msg: %s" % (self.error_code, self.error_message)).log_error()
        return {'error': self.error_code}


class NotFoundException(BaseCustomException):
    status_code = 404
    error_message = NOT_FOUND_404
