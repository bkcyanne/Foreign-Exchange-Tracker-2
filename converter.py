#Python program to convert currency based on specific value

import requests
import PySimpleGUI as sg

class Currencyconverter:
    #empty dictionary to store conversion rates
    rates = {}
    def __init__(self,url):
        data = requests.get(url).json()

        #Extracting only rates from the json data
        self.rates = data["rates"]

    #the function to calculate conversions
    def convert(self,from_curr,to_curr,amt):
        initial_amt = amt
        if from_curr != 'EUR':
            amt = amt / self.rates[from_curr]

        #limiting to 2 decimal places
        amt = round(amt * self.rates[to_curr], 2)
        return amt
        
        
#Driver
if __name__ == "__main__":
    access_key = 'a809c9c1baff704d89c53f0684c9b365'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=',access_key)
    c = Currencyconverter(url)
    subscriptions = []
    
    layout = [  [sg.Text("Foreign Exchange Tracker")], 
                [sg.Text('From Currency: ', size=(15, 1)), sg.InputText(key='fromcurr')], 
                [sg.Text('To Currency: ', size=(15, 1)), sg.InputText(key='tocurr')],
                [sg.Text('Value: ', size=(15, 1)),sg.InputText(key='val')], 
                [sg.Button('Calculate'), sg.Button('Exit')], 
                [sg.Text('Output: ', size=(15, 1)),sg.Text('                  ', size=(25, 1),key="rate")],
                [sg.Button('New Calculation'), sg.Button('Subscribe to Currency Pair',key='subscribe')],
                [sg.Text("Daily Updates: ", key="updatesempty")],
                [sg.Text("From Currency: "), sg.Text('     ', size=(25, 1),key="dailyfrom"),sg.Text("To Currency: "), sg.Text('    ', size=(25, 1),key="dailyto"), sg.Text("Value: "), sg.Text('  ', size=(25, 1),key="dailyval"),  sg.Text("EntEr Value to Check: "), sg.InputText(key='val2')],
                [sg.Button('Calculate Subscriptions')]]


    window = sg.Window("Foreign Exchange Tracker", layout).Finalize()
    newval = 0

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Calculate':
            fromcurrency = str(values['fromcurr'])
            tocurrency = str(values['tocurr'])
            amount = float(values['val'])
            newval = c.convert(fromcurrency,tocurrency,amount)
            window['rate'].update(newval)

        if event == 'Subscribe to Currency Pair':
            subscriptions.append([values['fromcurr'],values['tocurr']])
            for i in subscriptions:
                window['dailyfrom'].update(i[0])
                print(str(values['dailyfrom']))
                window['dailyto'].update(i[1])

        if event == 'New Calculation':
            layout = [  [sg.Text("Foreign Exchange Tracker")], 
                [sg.Text('From Currency: ', size=(15, 1)), sg.InputText(key='fromcurr')], 
                [sg.Text('To Currency: ', size=(15, 1)), sg.InputText(key='tocurr')],
                [sg.Text('Value: ', size=(15, 1)),sg.InputText(key='val')], 
                [sg.Button('Calculate'), sg.Button('Exit')], 
                [sg.Text('Output: ', size=(15, 1)),sg.Text('                  ', size=(25, 1),key='rate')],
                [sg.Button('New Calculation'), sg.Button('Subscribe to Currency Pair',key='subscribe')],
                [sg.Text("Daily Updates: ", key="updatesempty")],
                [sg.Text("From Currency: "), sg.Text('     ', size=(25, 1),key='dailyfrom'),sg.Text("To Currency: "), sg.Text('    ', size=(25, 1),key='dailyto'), sg.Text("Value: "), sg.Text('  ', size=(25, 1),key="dailyval"),  sg.Text("Enter Value to Check: "), sg.InputText(key='val2')],
                [sg.Button('Calculate Subscriptions')]]

            window = sg.Window("Foreign Exchange Tracker", layout).Finalize()




    window.close()







