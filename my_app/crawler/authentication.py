class Authentication:

    @staticmethod
    def validate(api_key, type_return):
        """
        --> Validate if information base for next
        :param api_key:
        :param type_return:
        :return: Msg error or null
        """
        validate_token = Authentication.validate_api_key(api_key)
        if validate_token:

            return validate_token
        if type_return != 'json' and type_return != 'xml':

            return 'param_return incorrect'

    @staticmethod
    def validate_api_key(api_key):
        """
        --> Validate api_key
        :type api_key: str
        :param api_key: key of authentication
        :return: true or false
        """
        if api_key != 'eyJuYW1lIjoiR2FicmllbCBDYXN0b3Jpbm8ifQ':

            return 'access denied'

        return False
