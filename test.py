from app import app
from unittest import TestCase


class CurrencyConverterTestCase(TestCase):
    def test_form_page(self):
        '''Make sure home page has status 200 OK'''

        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<h1 class="display-6 text-center">Currency Converter</h1>', html)

    def test_result_page(self):
        '''Make sure page goes to result.html if correct input values are entered'''

        with app.test_client() as client:
            res = client.get('/result?conv_from=usd&conv_to=usd&amount=1')
            html = res.get_data(as_text=True)
            self.assertIn('Make another conversion', html)
