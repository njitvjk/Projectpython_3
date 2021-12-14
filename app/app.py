"""A simple flask web app"""
import re
from csv import DictWriter

import pandas
import pandas as pd
from flask import Flask, request, url_for
from flask import render_template
from calc.calculator import Calculator
from calc.history.calculations import Calculations

app = Flask(__name__)


@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')


@app.route("/basicform", methods=['GET', 'POST'])
def calculator():
    """bad calc Route Response"""

    if request.method == 'POST':
        # get the values out of the form
        m = re.match(r'^\-?\d*[.@]?\d*$', request.form['value1'])
        n = re.match(r'^\-?\d*[.@]?\d*$', request.form['value2'])
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Invalid Input: A value for operation cannot be empty.'
            return render_template('basicform.html', error=error)
        elif m is None or n is None:
            error = 'Invalid Input: Values can only be numeric or float'
            return render_template('basicform.html', error=error)
        elif n is None:
            error = 'Invalid Input: Values can only be numeric or float'
            return render_template('basicform.html', error=error)

        else:
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())

            data = {
                'OPERATION': [operation],
                'VALUE_A': [value1],
                'VALUE_B': [value2],
                'RESULT': [result]
            }

            # Calculator.writeHistoryToCSV(data)
            operations = pd.DataFrame(data)
            operations.to_csv('operationsdata.csv', mode='a', index=False, header=False)
            # Pass the CSV  file object to the Dictwriter() function
            data = pandas.read_csv('operationsdata.csv', header=0)
            myData = data.values

            # with open('operationdata.csv', 'a', newline='') as f_object:
            # Pass the CSV  file object to the Dictwriter() function
            # Result - a DictWriter object
            # dictwriter_object = DictWriter(f_object)
            # Pass the data in the dictionary as an argument into the writerow() function
            # dictwriter_object.writerow(data)
            # Close the file object
            # f_object.close()
            return render_template('basicform.html', value1=value1, value2=value2, operation=operation, result=result,
                                   calculation_performed=True,myData=myData)
            # Displays the form because if it isn't a post it is a get request
    elif request.method == 'GET':
        return render_template('basicform.html')


@app.route("/calculator")
def basicform():
    """Post Request Handling"""
    return render_template('calculator.html')
