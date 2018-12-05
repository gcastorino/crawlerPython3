from unittest import TestCase, main
from my_app.crawler.authentication import Authentication


class Test(TestCase):
    def test_validate_token_false(self):
        self.assertEqual(Authentication.validate_token('teste'), False)

    def test_validate_token_true(self):
        self.assertEqual(Authentication.validate_token('123'), 'access denied')

    def test_validate(self):
        self.assertEqual(Authentication.validate('teste', '123'), 'param_return incorrect')


if __name__ == '__main__':
    main()
