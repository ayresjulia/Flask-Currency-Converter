from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chickenzarecool21837'

c = CurrencyRates()
code = CurrencyCodes()
supported_c = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD',
               'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']


@app.route('/')
def form_page():
    '''Currency form page'''

    return render_template('index.html')


@app.route('/result')
def result_page():
    '''Converts currency and shows result, if currecy abbreviation is valid'''

    conv_from = request.args['conv_from'].upper()  
    conv_to = request.args['conv_to'].upper()  
    amount = int(request.args['amount'])  
    abbr = code.get_symbol(conv_to)  
    if conv_from not in supported_c:
        flash('Currency not supported, try again', 'alert alert-danger')
        return redirect('/')
    elif conv_to not in supported_c:
        flash('Currency not supported, try again', 'alert alert-danger')
        return redirect('/')
    else:
        converted_amt = c.convert(conv_from, conv_to, amount)
        abbr = code.get_symbol(conv_to)  
        flash('Success!', 'alert alert-success')
    return render_template('result.html', conv_from=conv_from, conv_to=conv_to, amount=amount, converted_amt=converted_amt, abbr=abbr)
