from unittest import TestCase, main
from my_app.crawler.authentication import Authentication


class Test(TestCase):
    def test_validate_api_key_false(self):
        self.assertEqual(Authentication.validate_api_key('eyJuYW1lIjoiR2FicmllbCBDYXN0b3Jpbm8ifQ'), False)

    def test_validate_api_key_true(self):
        self.assertEqual(Authentication.validate_api_key('123'), 'access denied')

    def test_validate(self):
        self.assertEqual(
            Authentication.validate('eyJuYW1lIjoiR2FicmllbCBDYXN0b3Jpbm8ifQ', '123')
            , 'param_return incorrect'
        )


if __name__ == '__main__':
    main()
