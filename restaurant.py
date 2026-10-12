
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from AIT!'


menu = {}
history = []
summary = {'total': 0, 'count': 0, 'orders': 0, 'gotovitsa': 0}

zakazi = {}

# client
# povar
# owner/admin
# courier

@app.route('/dobav_menu')
def dobav_v_menu():
    d = request.args
    if 'name' in d and 'price' in d and 'qty' in d:
        name = d['name']
        price = int(d['price'])
        qty = int(d['qty'])

        if name in menu:
            menu[name]['price'] = price
            menu[name]['qty'] += qty
        else:
            menu[name] = {'price':price, 'qty': qty}
        return jsonify(menu)
    else:
        return '<h1>NORMALNIY BOL EE</h1>'


@app.route('/zakaz')
def primi_zakaz():
        d = request.args
        if 'client' in d and 'names' in d:
            client = d['client']
            names = d['names']

            orders = []
            total = 0
            for name in names.split(','):
                qty = 1
                if name in menu and qty <= menu[name]['qty']:
                    orders.append((name, qty))
                    menu[name]['qty'] -= qty
                    total += qty * menu[name]['price']
                    summary['count'] += qty

            summary['orders'] += 1
            summary['total'] += total
            summary['gotovitsa'] += 1

            zakazi[client] = {'order': orders, 'total': total, 'status': 'gotovim'}
            history.append( (client, total, orders) )
            return jsonify(zakazi)
        else:
            return 'NORMALNIY KIRBEYSIN BI'


@app.route('/otchet')
def otchet():
    return summary

@app.route('/gotov')
def povar():
    d = request.args
    if 'client' in d:
        client = d['client']
        if client in zakazi:
            zakazi[client]['status'] = 'gotov'
            summary['gotovitsa'] -= 1
        return jsonify(zakazi)
    else:
        return "NORMALNIY KIRBEYSIN BI"


@app.route('/courier')
def courier():
    d = request.args
    if 'client' in d:
        client = d['client']
        if client in zakazi and zakazi[client]['status'] == 'gotov':
            del zakazi[client]
            return 'ZAKAZ UDALSYA'
        else:
            return 'ZAKAZ BUTO ELEK'
    else:
        return 'NORMALNIY BOLBOYSUN BU EE'

@app.route('/pokaji_zakazi')
def pokaji_zakazi():
    return jsonify(zakazi)



app.run()