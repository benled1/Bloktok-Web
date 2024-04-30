
class RedditParserException(Exception):
    pass


class UnexpectedResponseFormat(RedditParserException):
    def __init__(self, message):
        super().__init__(message)