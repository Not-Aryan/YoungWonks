import bson
from flask import *
import flask
import bson.objectid
import flask_bootstrap
import flask_pymongo
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import random


app = Flask("one-stop-project2")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/one-stop-project-db"
app.config['SECRET_KEY'] = 'plzwork'

Bootstrap(app)
mongo = PyMongo(app)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add_product.html')
    elif request.method == 'POST':
        doc = {}
        data = request.form
        for item in request.form:
            doc[item] = request.form[item]
        mongo.db.products.insert_one(doc)
        return redirect('/')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        session['cart-items'] = {}
        found_products = mongo.db.products.find({})
        lst = [x for x in found_products]
        a = lst
        k = int(len(lst))
        return render_template('buy.html', products=lst)
    elif request.method == 'POST':
        doc = {}
        for item in request.form:
            # print(type(item))
            # print(item['_id'])
            # print(request.form[item])
            if int(request.form[item]) != 0:
                doc[item] = request.form[item]
            else:
                print("NOTHING")
        print(request.form)
        session['cart-items'] = doc
        return redirect('/checkout')


@app.route('/checkout')
def checkout():
    total = 0
    cart_items = []
    # print(type(session['cart-items']))
    stored_info = session['cart-items']
    #print(type(stored_info))
    # print(type(stored_info), stored_info)
    # print(stored_info['_id'])
    for ID in stored_info:
        # print(type(ID))
        found_item = mongo.db.products.find_one({'_id': ObjectId(ID)})
        found_item['bought'] = stored_info[ID]
        found_item['item-total'] = int(found_item['price']) * int(found_item['bought'])
        bob = found_item['item-total']
        print("THIS ONE", found_item['item-total'])
        cart_items.append(found_item)
        total += bob
    print(cart_items)
    return render_template('checkout.html', products=cart_items, total=total)


app.run(debug=True)
