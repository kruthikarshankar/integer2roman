from django.shortcuts import render
from converter.forms import ConverterForm
from utils import int2roman


def converter_view(request):

    '''
        Defines the view for Converting an Integer to Roman numeral.
        :param request:
        :return: form with integer and/or roman numeral
    '''

    form = ConverterForm()
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            integer = cleaned_data.get('integer')
            request.integer = integer
            request.result = int2roman(integer)
            return render(request, 'converter.html', {'form': form})

    return render(request, 'converter.html', {'form': form})
