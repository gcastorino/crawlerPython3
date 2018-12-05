class Authentication:

    @staticmethod
    def validate(auth, type_return):
        """
        --> Validate if information base for next
        :param auth:
        :param type_return:
        :return: Msg error or null
        """
        validate_token = Authentication.validate_token(auth)
        if validate_token:

            return validate_token
        if type_return != 'json' and type_return != 'xml':

            return 'param_return incorrect'

    @staticmethod
    def validate_token(auth):
        """
        --> Validate token
        :type auth: str
        :param auth: token of authentication
        :return: true or false
        """
        if auth != 'teste':

            return 'access denied'

        return False
