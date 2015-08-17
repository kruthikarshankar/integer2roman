from django import forms

__author__ = 'kruthika'


class ConverterForm(forms.Form):
    '''
        Form definition for integer to roman numeral conversion
    '''
    integer = forms.IntegerField(initial=1, min_value=1, max_value=3999, required=True)

