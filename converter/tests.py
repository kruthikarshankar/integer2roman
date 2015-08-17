from django.core.urlresolvers import reverse
from converter.forms import ConverterForm
from utils import int2roman as roman
from utils import OutOfRangeError, NotAnIntegerError
import unittest


# Test case for converter view.
def test_converter_view(self):
    test_integer = 23
    url = reverse("converter")
    resp = self.client.get(url, {'integer': test_integer})
    self.assertEqual(resp.status_code, 200)
    self.assertIn(resp.content)


# Test case for valid form
def test_valid_form(self):
    data = {'integer': 23,}
    form = ConverterForm(data=data)
    self.assertTrue(form.is_valid())


# Test case for invalid form
def test_invalid_form(self):
    data = {'integer': 4000,}
    form = ConverterForm(data=data)
    self.assertFalse(form.is_valid())


class TestConverter(unittest.TestCase):
    '''
        Test cases for actual conversion from integer to roman numeral
    '''

    def test_int2roman(self):
        self.assertEqual(roman(1), 'I')
        self.assertEqual(roman(2013), 'MMXIII')

    def test_int2roman_errors(self):
        self.assertRaises(OutOfRangeError, roman, 100000)
        self.assertRaises(NotAnIntegerError, roman, '1')


def test_suite():
    return unittest.makeSuite(TestConverter)
